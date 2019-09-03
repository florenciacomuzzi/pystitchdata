# coding=utf-8
class DestinationConfig(object):
    def __init__(self, dest_type, properties):
        self.type = dest_type
        self.properties = properties


class PostgresConfig(DestinationConfig):
    def __init__(self, host, port, username, database, password, ssl):
        # validate params
        dest_type = 'postgres'
        properties = {
            'host': host,
            'port': port,
            'username': username,
            'database': database,
            'password': password,
            'ssl': ssl
        }
        super().__init__(dest_type, properties)


class S3Config(DestinationConfig):
    def __init__(self, csv_delimiter, csv_force_quote, output_file_format,
                 s3_bucket, s3_key_format_string):
        # TODO validate params
        # TODO add credentials params
        dest_type = 's3'
        properties = {
            "csv_delimiter": csv_delimiter,
            "csv_force_quote": csv_force_quote,
            "output_file_format": output_file_format,
            "s3_bucket": s3_bucket,
            "s3_key_format_string": s3_key_format_string,
        }
        super().__init__(dest_type, properties)
