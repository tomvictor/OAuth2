from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from accesstoken.serializers import RefreshTokenSerializer, UserLoginSerializer


class UserLoginView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=serializer.validated_data["username"])
        resfretoken = RefreshToken.for_user(user)
        response = {
            "success": "True",
            "status code": status.HTTP_200_OK,
            "message": "User logged in  successfully",
            "token": serializer.data["token"],
            "resfretoken": str(resfretoken),
        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)


class RefreshTokenView(TokenRefreshView):
    permission_classes = [AllowAny]
    serializer_class = RefreshTokenSerializer
