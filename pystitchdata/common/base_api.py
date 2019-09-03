"""
This module provides the base structures necessary to interact with an API.
"""
import json
import logging
from pprint import pprint

import requests

from retrying import retry

from pystitchdata import config
from pystitchdata.common import enums, exceptions

logger = logging.getLogger(__name__)


class BaseAPI(object):

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(self.authenticate())

    def authenticate(self):
        """Authenticate to the API using the relevant auth mechansim.
        Args:
            auth_mechanism (enums.APIAuthMechanism): The auth mechanism to use
        Returns:
            a session.auth Object
        """
        return {'Authorization': 'Bearer ' + config.AUTH_TOKEN}
        # if auth_mechanism == enums.APIAuthMechanism.BASIC:
        #     return requests.auth.HTTPBasicAuth(self.user, self.token)
        # elif auth_mechanism == enums.APIAuthMechanism.DIGEST:
        #     return requests.auth.HTTPDigestAuth(self.user, self.token)

    def _get_url(self, uri):
        """Handle conversion of a partial URL."""
        # if uri is a full url, use it
        if uri.startswith('https://'):
            url = uri
        else:
            url = '{}{}'.format(config.BASE_URL, uri)
        return url

    def get_next_page(self, res, header, uri):
        """Custom logic to retrieve the next page in a paginated result.
        The child class should define this logic based on the specifics
        of the API being scraped.
        Args:
            res    : result of uri call
            header : header of resulting api call
            uri    : original uri
        """
        return None

    def custom_error_handling(exception):
        """Return True if we should retry the API call, False otherwise.
        Default behaviour is to not retry.
        Args:
            exception (APIException): An exception object to introspect and
                determine the best course of action
        """
        return False

    @retry(wait_fixed=30000, retry_on_exception=custom_error_handling)
    def __single_query_api(self, uri):
        """Issue a query to the API.
        Args:
            uri (str): The URI to query
        Returns:
            The raw HTTP response
        """
        url = self._get_url(uri)
        r = self.session.get(url)
        try:
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            try:
                errormessage = str(e) + " - " + e.response.json().get("error")
            except json.decoder.JSONDecodeError:
                errormessage = '{status_code} {reason}'.format(
                    status_code=e.response.status_code,
                    reason=e.response.reason)
            raise exceptions.APIException(
                errormessage,
                status_code=e.response.status_code)
        return r

    def __parse_result(self, text):
        """Parse the text returned from the API result into JSON.
        Args:
            text : The text as it appears in the raw HTTP response
        Returns:
            HTTP response data formatted as JSON
        """
        try:
            data = json.loads(text)
        except ValueError as e:
            msg = "Invalid JSON received: %s" % str(e)
            raise exceptions.APIException(msg)
        return data

    def query_api(self, uri):
        """Issue a HTTP GET request at the API.
        Args:
            uri (str): The URI to hit.
        Returns:
            The full dataset returned from a single logical API call as an
                array of dicts (or an empty array if no data in HTTP response)
        """
        raw = self.__single_query_api(uri)
        res = self.__parse_result(raw.text)
        header = raw.headers
        # collect all data associated with an API call (including paginated
        # results) into a single array
        results = []
        while res:
            if isinstance(res, dict):
                res = [res]
            results += res
            # If the HTTP response is paginated, issue a followup API call to
            # retrieve all remaining results
            uri = self.get_next_page(res, header, uri)
            if uri is not None:
                raw = self.__single_query_api(uri)
                res = self.__parse_result(raw.text)
                header = raw.headers
                continue
            else:
                break
        return results


if __name__ == '__main__':
    api = BaseAPI()
    r = api.query_api()
    pprint(r)
