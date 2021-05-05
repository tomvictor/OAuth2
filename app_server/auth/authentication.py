from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomJWTAuthentication(JWTAuthentication):
    # TODO : overide the authenticate and cjeck the token exists in the db
    pass
