class OAuthHandler(object):
    AUTHORIZATION_URL = ""
    ACCESS_TOKEN_URL = ""
    ACCESS_TOKEN_METHOD = 'POST'
    client_id = ""
    client_secret = ""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def refresh_token(self) -> str:
        return ""

    def access_token(self) -> str:
        return ""
