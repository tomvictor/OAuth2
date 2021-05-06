from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.views import TokenRefreshView

from .models import User
from .serializers import UserDetailSerializer


class RefreshAPIView(TokenRefreshView):
    """Refresh API

    Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.
    """

    permission_classes = [AllowAny]
    serializer_class = TokenRefreshSerializer


class LoginAPIView(GenericAPIView):
    """Login API

    Authenticates the user credentials and respond with valid
    access token and refresh token.

    """

    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class UserProfileAPIView(RetrieveAPIView):
    """User Profile API

    Return the detailed information of the authenticated user.

    """

    permission_classes = [IsAuthenticated]
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user
