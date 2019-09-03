# coding=utf-8
class Property(object):
    def __init__(self, name, is_required, is_credential, system_provided,
                 property_type, json_schema, provided, tap_mutable):
        self.name = name
        self.is_required = is_required
        self.is_credential = is_credential
        self.system_provided = system_provided
        self.property_type = property_type
        self.json_schema = json_schema
        self.provided = provided
        self.tap_mutable = tap_mutable
