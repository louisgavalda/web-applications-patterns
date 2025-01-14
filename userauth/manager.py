from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError


class CutomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email or email is None:
            raise ValidationError("User must have email address")
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
