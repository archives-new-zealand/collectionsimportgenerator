"""Tests template."""

# pylint: disable=C0103,R0801

from typing import Final

import pytest

from src.collections_import.external_csv_handler import convert_dates
from src.collections_import.import_sheet_generator import (
    ImportGenerationException,
    get_hash,
    import_sheet_generator,
)


def test_convert_dates():
    """Provide some basic date conversion tests."""
    date = "1/2/2024"
    assert convert_dates(date) == "2024"
    assert convert_dates(date, False) == "2024-02-01"
    # If the date can't be converted because it is already the correct
    # format for some other unknown type then the data is returned
    # as-is.
    date = "2024-01-01"
    assert convert_dates(date) == date
    date = "random data"
    assert convert_dates(date) == date


def test_get_hash():
    """Provide some basic testing for get hash."""
    test_row = {"MD5_HASH": "cafef00d"}
    assert get_hash(test_row) == "cafef00d"
    test_row = {"NOHASH": "badf00d"}
    with pytest.raises(ImportGenerationException) as exception_info:
        get_hash(test_row)
    assert "hashes aren't configured" in str(exception_info.value)


json_schema: Final[
    str
] = """
{
    "title": "Archives New Zealand - Archway Import Sheet Schema",
    "description": "Draft schema for validating CSV files for import into Archway at Archives New Zealand.",
    "validator": "http://csvlint.io/",
    "standard" : "http://dataprotocols.org/json-table-schema/",
    "fields": [
        {
            "name": "MissingReason",
            "description": "A description of the field we're describing here.",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "MissingComment",
            "description": "A description of the field we're describing here.",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "AgencyIdentifierScheme",
            "description": "AgencyIdentifierScheme",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "Language",
            "description": "Language from agency",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "AuthenticityIntegrity",
            "description": "AuthenticityIntegrity",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "item-agy-transferring-reference",
            "description": "Agency Code",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "item-ser-actual-reference",
            "description": "Actual Series",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "BoxNumber",
            "description": "A description of the field we're describing here.",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "PositionReference",
            "description": "Item No.",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "RecordNumber",
            "description": "A description of the field we're describing here.",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "PartNumber",
            "description": "A description of the field we're describing here.",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "SepFlag",
            "description": "A description of the field we're describing here.",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "SepNumber",
            "description": "A description of the field we're describing here.",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "Name",
            "description": "Title",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "AlternativeName",
            "description": "A description of the field we're describing here.",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "Creator",
            "description": "A description of the field we're describing here.",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "YearStartQualifier",
            "description": "A description of the field we're describing here.",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "YearStart",
            "description": "A description of the field we're describing here.",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "YearEndQualifier",
            "description": "A description of the field we're describing here.",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "YearEnd",
            "description": "A description of the field we're describing here.",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "ContentRestrictionStatus",
            "description": "Content Restriction Status",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "ContentRestrictionExpiryType",
            "description": "Content Restriction Expiry Type",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "ContentRestrictionExpiryYear",
            "description": "A description of the field we're describing here.",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "ContentRestrictionAutoExpiry",
            "description": "ContentRestrictionAutoExpiry",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "MetadataRestrictionStatus",
            "description": "Metadata Restriction Status",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "MetadataRestrictionExpiryType",
            "description": "MetadataRestrictionExpiryType",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "MetadataRestrictionExpiryYear",
            "description": "MetadataRestrictionExpiryYear",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "MetadataRestrictionAutoExpiry",
            "description": "MetadataRestrictionAutoExpiry",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "IssuableStatus",
            "description": "Preservation Status",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "RecordNumberAlternative",
            "description": "A description of the field we're describing here.",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "FormerArchivesReference",
            "description": "A description of the field we're describing here.",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "ContentType",
            "description": "Record Type",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "AdditionalDescriptionItem",
            "description": "Description",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "EntityType",
            "description": "Item Level",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "DigitalItemsOnly",
            "description": "DigitalItemsOnly",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "ItemLevel",
            "description": "Item Level",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "Current",
            "description": "Current",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "item-acc-part-of-reference",
            "description": "Accession Number",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "RepositoryReference",
            "description": "Repository Reference",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "HoldingsLocation",
            "description": "Repository",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "RulesUsed",
            "description": "RulesUsed",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "DocumentationStandard",
            "description": "DocumentationStandard",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        },
        {
            "name": "ProvenanceNote",
            "description": "ProvenanceNote",
            "type": "http://www.w3.org/2001/XMLSchema#string"
        }
    ]
}
"""

droid_csv: Final[
    str
] = """
ID,PARENT_ID,URI,FILE_PATH,NAME,METHOD,STATUS,SIZE,TYPE,EXT,LAST_MODIFIED,EXTENSION_MISMATCH,MD5_HASH,FORMAT_COUNT,PUID,MIME_TYPE,FORMAT_NAME,FORMAT_VERSION
1,,file://tmp/collections_test/carlys_file.pdf,/tmp/collections_test/carlys_file.pdf,carlys_file.pdf,,Done,6,File,pdf,2024-06-08T14:18:30+02:00,FALSE,edc3d3797971f12c7f5e1d106dd5cee2,0,,,,
2,,file://tmp/collections_test/jans_file.pdf,/tmp/collections_test/jans_file.pdf,jans_file.pdf,,Done,6,File,pdf,2024-06-08T14:18:22+02:00,FALSE,ab3c103dfee69624c486b74d3c90db65,0,,,,
3,,file://tmp/collections_test/joshuas_file.pdf,/tmp/collections_test/joshuas_file.pdf,joshuas_file.pdf,,Done,6,File,pdf,2024-06-08T14:18:42+02:00,FALSE,9c1f47efb9e8ab0afc87c2e04fe66b95,0,,,,
"""

external_csv: Final[
    str
] = """
Content Description,Record No.,Created Date,Created Date/Time,Created Time,Custodian,File Extension,File Name,File Size,File Type,Last Accessed Date,Last Accessed Date/Time,Last Accessed Time,Last Modified Date,Last Modified Date/Time,Last Modified Time,MD5 Hash,Media Type,Original File Extension,FILE_PATH,Character Data
Description of file One,ANZ12345,4/12/2022,12/4/2023 2:15 PM,02:15:16 PM,New Zealand Lettuce growers association (🥬),PDF,collections_test/carlys_file.pdf,3947345,Adobe Portable Document Format,8/12/2020,12/8/2020 1:27 PM,01:27:52 PM,4/12/2020,12/4/2020 2:15 PM,02:15:16 PM,edc3d3797971f12c7f5e1d106dd5cee2,application/pdf,PDF,/tmp/collections_test/carlys_file.pdf,"ā, ē, ī, ō, ū, Ā, Ē, Ī, Ō Ū"
Description of file Two,ANZ01234,4/12/2020,12/4/2020 1:47 PM,01:47:26 PM,New Zealand Lettuce growers association (🥬),PDF,collections_test/jans_file.pdf,252381,Adobe Portable Document Format,8/12/2020,12/8/2020 1:27 PM,01:27:52 PM,4/12/2020,12/4/2020 2:11 PM,02:11:40 PM,ab3c103dfee69624c486b74d3c90db65,application/pdf,PDF,/tmp/collections_test/jans_file.pdf,"ā, ē, ī, ō, ū, Ā, Ē, Ī, Ō Ū"
Description of file Three,ANZ23456,4/12/2020,12/4/2020 1:47 PM,01:47:26 PM,New Zealand Lettuce growers association (🥬),PDF,collections_test/joshuas_file.pdf,123,Adobe Portable Document Format,8/12/2020,12/8/2020 1:27 PM,01:27:52 PM,4/12/2020,12/4/2020 2:11 PM,02:11:40 PM,9c1f47efb9e8ab0afc87c2e04fe66b95,application/pdf,PDF,/tmp/collections_test/joshuas_file.pdf,"ā, ē, ī, ō, ū, Ā, Ē, Ī, Ō Ū"
"""

conf: Final[
    str
] = """
[droid mapping]

AuthenticityIntegrity=MD5_HASH
Name=FILE_PATH

[static values]

item-agy-transferring-reference=
item-ser-actual-reference=
DigitalItemsOnly=
ContentRestrictionStatus=
ContentRestrictionExpiryType=
ContentRestrictionExpiryYear=
ContentRestrictionAutoExpiry=Split Enz
MetadataRestrictionStatus=
MetadataRestrictionExpiryType=
MetadataRestrictionExpiryYear=
MetadataRestrictionAutoExpiry=Alice Cooper
IssuableStatus=
ContentType=♙♘♗♖♕♔♚♛♜♝♞♟
ItemLevel=
EntityType=
Current=
item-acc-part-of-reference=
RepositoryReference=
HoldingsLocation=
RulesUsed=
DocumentationStandard=

[additional values]

pathmask=/tmp/

[external mapping config]

PathColumn=FILE_PATH
Mask=
ChecksumColumn = MD5 Hash
Date Pattern = ^[1-9]\\d?\\/\\d{2}\\/\\d{4}$

[external mapping]

AuthenticityIntegrity=
Creator=Custodian
MissingReason=
MissingComment=Content Description
BoxNumber=
PositionReference=
RecordNumber=
PartNumber=
SepFlag=
SepNumber=
Name=
AlternativeName=Last Modified Time
AgencyIdentifierScheme=
Language=
YearStartQualifier=
YearStart=Created Date
YearEndQualifier=
YearEnd=
ContentRestrictionStatus=
ContentRestrictionExpiryType=
ContentRestrictionExpiryYear=
MetadataRestrictionStatus=
MetadataRestrictionExpiryType=
MetadataRestrictionExpiryYear=
IssuableStatus=
RecordNumberAlternative=
FormerArchivesReference=
ContentType=
AdditionalDescriptionItem=
EntityType=
ItemLevelLegacy=
RepositoryReference=
ProvenanceNote=Character Data
"""

res: Final[
    str
] = """
"MissingReason","MissingComment","AgencyIdentifierScheme","Language","AuthenticityIntegrity","item-agy-transferring-reference","item-ser-actual-reference","BoxNumber","PositionReference","RecordNumber","PartNumber","SepFlag","SepNumber","Name","AlternativeName","Creator","YearStartQualifier","YearStart","YearEndQualifier","YearEnd","DigitalItemsOnly","ContentRestrictionStatus","ContentRestrictionExpiryType","ContentRestrictionExpiryYear","ContentRestrictionAutoExpiry","MetadataRestrictionStatus","MetadataRestrictionExpiryType","MetadataRestrictionExpiryYear","MetadataRestrictionAutoExpiry","IssuableStatus","RecordNumberAlternative","FormerArchivesReference","ContentType","AdditionalDescriptionItem","EntityType","ItemLevel","Current","item-acc-part-of-reference","RepositoryReference","HoldingsLocation","RulesUsed","DocumentationStandard","ProvenanceNote"
"","Description of file One","","","edc3d3797971f12c7f5e1d106dd5cee2","","","","","","","","","collections_test/carlys_file.pdf","02:15:16 PM","New Zealand Lettuce growers association (🥬)","","2022","","","","","","Split Enz","","","","Alice Cooper","","","","♙♘♗♖♕♔♚♛♜♝♞♟","","","","","","","","","","ā, ē, ī, ō, ū, Ā, Ē, Ī, Ō Ū"
"","Description of file Two","","","ab3c103dfee69624c486b74d3c90db65","","","","","","","","","collections_test/jans_file.pdf","02:11:40 PM","New Zealand Lettuce growers association (🥬)","","2020","","","","","","Split Enz","","","","Alice Cooper","","","","♙♘♗♖♕♔♚♛♜♝♞♟","","","","","","","","","","ā, ē, ī, ō, ū, Ā, Ē, Ī, Ō Ū"
"","Description of file Three","","","9c1f47efb9e8ab0afc87c2e04fe66b95","","","","","","","","","collections_test/joshuas_file.pdf","02:11:40 PM","New Zealand Lettuce growers association (🥬)","","2020","","","","","","Split Enz","","","","Alice Cooper","","","","♙♘♗♖♕♔♚♛♜♝♞♟","","","","","","","","","","ā, ē, ī, ō, ū, Ā, Ē, Ī, Ō Ū"
"""


def test_basic_output_and_mapping(tmp_path):
    """Ensure a sheet can be generated with expected values"""

    collection = tmp_path / "collection"
    collection.mkdir()
    droid_file = collection / "droid.csv"
    external_md_file = collection / "external.csv"
    config_file = collection / "config.cfg"
    json_schema_file = collection / "schema.json"

    droid_file.write_text(droid_csv.strip(), encoding="utf-8")
    external_md_file.write_text(external_csv.strip(), encoding="utf-8")
    config_file.write_text(conf.strip(), encoding="utf-8")
    json_schema_file.write_text(json_schema.strip(), encoding="utf-8")

    import_csv = import_sheet_generator(
        droid_csv=droid_file,
        external_csv=external_md_file,
        import_schema=json_schema_file,
        config=config_file,
    )

    assert import_csv.strip() == res.strip()
