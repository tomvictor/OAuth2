from django.urls import path

from account import views

app_name = "auth"


urlpatterns = [
    path("v1/token/refresh/", views.RefreshAPIView.as_view(), name="token_refresh"),
    path("v1/login/", views.LoginAPIView.as_view(), name="login_api"),
    path("v1/profile/", views.UserProfileAPIView.as_view(), name="user_profile"),
]
