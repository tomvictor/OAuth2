from django.contrib.auth.models import AbstractUser
from django.db import models



class AuthBaseModel(models.Model):
    """Account Model base class inherited by all other classes."""

    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, AuthBaseModel):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "auth_user"
        ordering = ["first_name"]

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return self.get_full_name()


class AuthStore(AuthBaseModel):
    user = models.ForeignKey(User, null=False, blank=True, on_delete=models.CASCADE)
    access_token = models.TextField(null=False, blank=True)
    refresh_token = models.TextField(null=False, blank=True)
    data = models.JSONField(null=False, blank=True)

    class Meta:
        verbose_name = "Auth Store"
        verbose_name_plural = "Auth Stores"
        db_table = "auth_store"
        ordering = ["-id"]

    def __str__(self):
        return str(self.user)
