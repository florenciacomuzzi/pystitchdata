# coding=utf-8
from pprint import pprint

from pystitchdata.common import base_api
from pystitchdata.common.enums import HTTPMethod


class Destinations(base_api.BaseAPI):
    """
    Class for interacting with Stitchdata Destination object.

    Destinations are the data warehouses into which Stitch writes data.
    """
    URI = '/v4/destinations/{destination_id}'

    def __init__(self):
        super().__init__()

    def list_destinations(self):
        return self._destinations()

    def create_destination(self):
        # check for already existing destination... only 1 per acct
        raise NotImplementedError('create_destination method'
                                  ' is not implemented.')

    def update_destination(self):
        # Updates an existing destination.
        # Modifications to the type attribute are not supported.
        raise NotImplementedError('update_destination method'
                                  ' is not implemented.')

    def delete_destination(self):
        # Deletes an existing destination.
        # Note: Stitch requires a destination to replicate data. Replication
        # will be paused until a new destination
        # is created and has a successful
        # connection.
        raise NotImplementedError('delete_destination method'
                                  ' is not implemented.')

    def _destinations(self, destination_id=None, http_method=HTTPMethod.GET):
        if destination_id is None:
            uri = Destinations.URI.format(destination_id='')
        else:
            uri = Destinations.URI.format(destination_id)
        if http_method == HTTPMethod.GET:
            return self.query_api(uri)
        else:
            raise NotImplementedError('{} is not implemented.'
                                      .format(http_method))


if __name__ == '__main__':
    r = Destinations().list_destinations()
    pprint(r)
