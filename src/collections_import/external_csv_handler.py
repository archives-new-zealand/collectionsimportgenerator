"""External CSV handler."""

# pylint: disable=R0912,R1702,R0903,R0902

import configparser as ConfigParser
import logging
import re
from datetime import datetime
from os.path import exists

# pylint: disable=R0801

try:
    from droid_csv_handler import GenericCSVHandler
    from json_table_schema import json_table_schema
except ModuleNotFoundError:
    try:
        from src.collections_import.droid_csv_handler import GenericCSVHandler
        from src.collections_import.json_table_schema import json_table_schema
    except ModuleNotFoundError:
        from collections_import.droid_csv_handler import GenericCSVHandler
        from collections_import.json_table_schema import json_table_schema

logger = logging.getLogger(__name__)


def convert_dates(date: str, year: bool = True):
    """Return a year from a given date format."""
    try:
        dateobj = datetime.strptime(date, "%d/%m/%Y")
        if year:
            return dateobj.strftime("%Y")
        return dateobj.strftime("%Y-%m-%d")
    except ValueError:
        return date


class NewRow:
    """NewRow Object for access to CSV data."""

    checksum = ""
    path = ""
    rdict = {}

    def __init__(self):
        """Class Init."""
        self.rdict = {}  # shares memory if not initialized every call?


class ExternalCSVHandler:
    """Handler class for external CSV files."""

    # place to store cfg loc
    configfile = False

    # config section in cfg
    mapconfig = "external mapping config"

    # mapping section in cfg
    mapping = "external mapping"

    # data we want to read from the config file...
    pathcolumn = "PathColumn"
    checksumcolumn = "ChecksumColumn"
    pathmask = "Mask"
    datepattern = "Date Pattern"
    desctext = "descriptiontext"

    rowdict = {}
    maphead = []

    def __init__(self, configfile, importschema):
        self.config = ConfigParser.RawConfigParser()

        self.configfile = configfile
        self.importschema = importschema

        self.get_import_configuration()
        self.get_import_table_headers()

        self.get_mappings()

    def _checkconfig(self, section, name):
        """Provide a means to check a configuration file."""
        if self.config.has_option(section, name):
            var = self.config.get(section, name)
            return var
        return None

    def get_import_configuration(self):
        """Read the import config file which describes the mapping
        we need to convert an external CSV into an import sheet.
        """
        logger.info("mapping config being read from: '%s'", self.configfile)
        self.config.read(self.configfile, encoding="utf-8")
        self.pathmask = self._checkconfig(self.mapconfig, self.pathmask)
        self.checksumcol = self._checkconfig(self.mapconfig, self.checksumcolumn)
        self.pathcol = self._checkconfig(self.mapconfig, self.pathcolumn)
        self.descriptiontext = self._checkconfig(self.mapping, self.desctext)
        self.userdatepattern = self._checkconfig(self.mapconfig, self.datepattern)
        if self.userdatepattern is not None:
            self.dates = re.compile(self.userdatepattern)

    # Read the import sheet headers from our CSV schema file...
    def get_import_table_headers(self):
        """Read the import table schema headers for our CSV file from
        the import schema declaration.
        """
        logging.info("import table schema being read from: %s", self.importschema)
        with open(self.importschema, "rb") as schema:
            importschemajson = schema.read()
            importschema = json_table_schema.JSONTableSchema(importschemajson)
            self.import_schema_headers = importschema.field_names

    def get_mappings(self):
        """Using the CSV headers, see if there is an entry in the
        config file for the information we're receiving in this class.
        """
        for header in self.import_schema_headers:
            if not self.config.has_option(self.mapping, header):
                continue
            mapvalue = self.config.get(self.mapping, header)
            if mapvalue == "":
                continue
            if len(mapvalue.split(",")) > 1:
                for value in mapvalue.split(","):
                    self.rowdict[value] = header
                    self.maphead.append(value)
            else:
                self.rowdict[mapvalue] = header
                self.maphead.append(mapvalue)

        logger.info("mapped fields ({external field: import field}): %s", self.rowdict)

    def read_external_csv(self, extcsvname):
        """Read the external CSV we want to extract metadata from..."""
        augmented = []  # augmented metadata
        exportlist = None
        if exists(extcsvname):
            csvhandler = GenericCSVHandler()
            exportlist = csvhandler.csv_as_list(extcsvname)
            # counter a blank sheet
            if len(exportlist) < 1:
                exportlist = None
            if exportlist is not None:
                for external_row in exportlist:
                    # we need to differentiate in case we get non-unique values
                    nscount = 0
                    row = NewRow()
                    if external_row[self.checksumcol] != "":
                        row.checksum = external_row[self.checksumcol]
                    if external_row[self.pathcol] != "":
                        row.path = external_row[self.pathcol].replace(self.pathmask, "")
                    for field in external_row:
                        if field in self.maphead:
                            data = external_row[field].strip()
                            if re.match(self.dates, data):
                                data = convert_dates(data)
                            if self.rowdict[field] == "Description":
                                if data != "":
                                    nscount += 1
                                    data = field + ": " + data
                                    data = "ns" + str(nscount) + ":" + data
                                    row.rdict[data] = self.rowdict[field]
                            else:
                                nscount += 1
                                data = f"ns{nscount}:{data}"
                                row.rdict[data] = self.rowdict[field]
                    if row.checksum != "":
                        augmented.append(row)

        return self._fixdescription(augmented)

    def splitns(self, value):
        """Split a namespace string."""
        return value.split(":", 1)[1]

    def _fixdescription(self, augmented_list):
        """Provide a means to correct a description field."""
        for row in augmented_list:
            newrow = {}
            desc = ""
            temprow = row.rdict

            # Declare these early to work with them below.
            opendate = ""
            close = ""

            for r in temprow:
                if temprow[r] == "Description":
                    desc = desc + self.splitns(r) + ". "
                elif temprow[r] == "Open Year":
                    opendate = self.splitns(r)
                    newrow[r] = opendate
                elif temprow[r] == "Close Year":
                    close = self.splitns(r)
                    newrow[r] = close
                else:
                    newrow[r] = temprow[r]

            if desc != "" and self.descriptiontext is not None:
                desc = desc + self.descriptiontext
                newrow[desc] = "Description"

            row.rdict = newrow

        return augmented_list
