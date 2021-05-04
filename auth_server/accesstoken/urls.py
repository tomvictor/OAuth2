from django.urls import include, path

from accesstoken import views as token_views

urlpatterns = [
    path("token/", token_views.UserLoginView.as_view(), name="user_token"),
    path("refreshtoken/", token_views.RefreshTokenView.as_view(), name="user_token"),
]
