from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.settings import api_settings

User = get_user_model()


def get_backends() -> TokenBackend:
    #
    token_backend = TokenBackend(
        api_settings.ALGORITHM,
        settings.OAUTH2_CLIENT_SECRET_KEY,
        api_settings.VERIFYING_KEY,
        api_settings.AUDIENCE,
        api_settings.ISSUER,
    )
    return token_backend
