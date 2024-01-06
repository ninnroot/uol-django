from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from app_auth.managers import CustomUserManager
from utility.models import BaseModel


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    """
    The user model
    """

    email = models.EmailField(unique=True)

    name = models.CharField(max_length=512)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = None
    user_permissions = None

    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    def __str__(self):
        return f"<User: {self.id} {self.email}>"

    class Meta:
        ordering = ("id",)
