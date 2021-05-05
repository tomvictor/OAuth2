from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
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
