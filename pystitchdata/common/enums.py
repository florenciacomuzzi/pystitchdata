# coding=utf-8
import enum


class HTTPMethod(enum.Enum):
    """HTTP methods supported."""

    GET = 'GET'
    POST = 'POST'
    DELETE = 'DELETE'
    PUT = 'PUT'


class DestinationTypes(enum.Enum):
    """Destination types supported."""

    AZURE_SQL_DW = 'azuresql_dw'
    POSTGRES = 'postgres'
    REDSHIFT = 'redshift'
    S3 = 's3'
    SNOWFLAKE = 'snowflake'


class OutputFileFormat(enum.Enum):
    """Output file formats supported."""
    JSONL = 'jsonl'
    CSV = 'csv'


class PropertyType(enum.Enum):
    """Property types supported."""
    READ_ONLY = 'read_only'
    USER_PROVIDED = 'user_provided'
    USER_PROVIDED_IMMUTABLE = 'user_provided_immutable'
    SYSTEM_PROVIDED_BY_DEFAULT = 'system_provided_by_default'
