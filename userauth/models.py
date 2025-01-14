import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from userauth.manager import CutomUserManager


# https://ilovedjango.com/django/authentication/custom-user-model-in-django/


class CustomUser(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(null=True, blank=True, max_length=100)
    last_name = models.CharField(null=True, blank=True, max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    created_by = models.ForeignKey(
        "CustomUser",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="custom_users",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CutomUserManager()

    def __str__(self):
        if self.last_name:
            if self.first_name:
                return f"{self.first_name} {self.last_name}"
            return self.last_name
        return f"{self.email}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
