import oauth2 as oauth

from urllib import urlencode
import hashlib

import random

# TODO: Create test cases for all functionality.

class LinkedinException(Exception):
    pass


class LinkedinAPI(object):
    """Method sig: (key, secret, redirect, authorization_code(optional))"""

    AUTHORIZATION_URL = 'https://www.linkedin.com/uas/oauth2/authorization'
    TOKEN_ACCESS_URL = 'https://www.linkedin.com/uas/oauth2/accessToken'
    client = None
    consumer = None

    def __init__(self,
                 consumer_key,
                 consumer_secret,
                 redirect,
                 authorization_code=None):
        """Method sig: (key, secret, redirect, authorization_code(optional))"""

        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.redirect = redirect

        self.consumer = oauth.Consumer(
            key=self.consumer_key,
            secret=self.consumer_secret)
        self.client = oauth.Client(self.consumer)

    @property
    def get_auth_url(self):
        """Generates authorization url."""

        return '%s?%s' % (self.AUTHORIZATION_URL, self.authorization_body)

    @property
    def authorization_body(self):
        """Creates the authorization POST params."""

        self.authorization_body = urlencode({
            'response_type': 'code',
            'client_id': self.consumer_key,
            'redirect_uri': self.redirect,
            'state': str(self._generate_random_string()),
        })

        return self.authorization_body

    def get_access_token(self, access_code, redirect_uri):
        if access_code:
            # Execute the following code that retrieves the access Token.
            request_params = {
                'grant_type': 'authorization_code',
                'code': access_code,
                'redirect_uri': redirect_uri,
                'client_id': self.consumer_key,
                'client_secret': self.consumer_secret,
            }
            print request_params
            resp, content = self.client.request(
                self.TOKEN_ACCESS_URL,
                "POST",
                body=urlencode(request_params))

            print resp
            print content
        else:
            raise LinkedinException("Missing access code.")

    def _generate_random_string(self):
        return hashlib.md5(
            '%s%s' % (random.randint() ** 20, self.consume_secret)).hexdigest()
