from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    """Account Model base class inherited by all other classes."""

    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, BaseModel):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "user"
        ordering = ["first_name"]

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return self.get_full_name()


class AuthStore(BaseModel):
    user = models.ForeignKey(
        User,
        null=False,
        blank=True,
        on_delete=models.CASCADE,
        related_name="auth_stores",
    )
    access_token = models.TextField(null=False, blank=True)
    refresh_token = models.TextField(null=False, blank=True)
    expires_in = models.PositiveIntegerField(default=3600, null=False, blank=True)
    token_type = models.CharField(
        max_length=256, default="Bearer", blank=True, null=False
    )
    data = models.TextField(null=False, blank=True)

    class Meta:
        verbose_name = "Auth Store"
        verbose_name_plural = "Auth Stores"
        db_table = "auth_store"
        ordering = ["-id"]

    def __str__(self):
        return str(self.user)
