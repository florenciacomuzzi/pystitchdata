# coding=utf-8
from pystitchdata.common import property
from pystitchdata.common.enums import PropertyType


class SalesforceProperties(object):
    def __init__(self):
        # TODO json schema
        self.anchor_time = property.Property(
            name='anchor_time', is_required=False, is_credential=False,
            system_provided=False, property_type=PropertyType.USER_PROVIDED,
            json_schema=None, provided=False, tap_mutable=False)
        self.api_type = property.Property(
            name='api_type', is_required=True, is_credential=False,
            system_provided=False,
            property_type=PropertyType.USER_PROVIDED_IMMUTABLE,
            json_schema=None, provided=False, tap_mutable=False)