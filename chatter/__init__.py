import requests
from requests.auth import AuthBase


class BearerTokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['Authorization'] = f'Bearer {self.token}'
        return r


class ChatterAuth:
    def __init__(self, username, password, client_id, client_secret, production=False):
        login_env = 'login' if production else 'test'
        self._url = f'https://{login_env}.salesforce.com/services/oauth2/token'

        response = requests.post(self._url, params={
            'username': username,
            'password': password,
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'password'
        })

        self.access_token = None
        self.instance_url = None

        if response.status_code == 200:
            json_data = response.json()
            self.access_token = json_data.get('access_token')
            self.instance_url = json_data.get('instance_url')


class Chatter:

    def __init__(self, auth, version='45'):
        self._auth = auth
        self._path = f'services/data/v{version}.0/chatter'

    def __getattr__(self, attr):

        def call_(data):
            _url = f"{self._auth.instance_url}/{self._path}/{attr.replace('_', '-')}"
            response = requests.post(
                url=_url,
                auth=BearerTokenAuth(self._auth.access_token),
                json=data)
            return response.json()

        return call_

