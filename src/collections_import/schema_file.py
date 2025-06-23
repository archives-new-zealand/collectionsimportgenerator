"""JSON schema file for Archives New Zealand Collections.

If this file needs to change it needs to be done in code for now which
might not be the best pattern going forward. We will default to the
file based option by default.
"""

from typing import Final

JSON_SCHEMA: Final[
    str
] = """{
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
