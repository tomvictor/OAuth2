from django.conf import settings


class OAuthHandler(object):
    AUTHORIZATION_URL = settings.OAUTH2_AUTHORIZATION_URL
    ACCESS_TOKEN_URL = "/api/login/"
    REFRESH_TOKEN_URL = "/api/token/refresh/"
    ACCESS_TOKEN_METHOD = "POST"
    CLIENT_ID = settings.OAUTH2_CLIENT_ID
    CLIENT_SECRET = settings.OAUTH2_CLIENT_SECRET_KEY

    def __init__(self, username, password, scope=None, grant_type=None):
        self.username = username
        self.password = password
        if scope is not None:
            self.scope = scope
        else:
            self.scope = settings.OAUTH2_DEFAULT_SCOPE

        if grant_type is not None:
            self.grant_type = grant_type
        else:
            self.grant_type = settings.OAUTH2_GRANT_TYPE

    def generate_payload(self)->dict:
        payload = {
            "grant_type": self.grant_type,
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "username": self.username,
            "password": self.password,
            "scope": self.scope,
        }
        return payload

    def generate_query_params(self)->str:
        params = ""
        return params

    def refresh_token(self) -> str:
        return ""

    def access_token(self) -> str:
        return ""
