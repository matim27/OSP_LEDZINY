from django.contrib.auth.base_user import BaseUserManager
from django.utils.crypto import get_random_string



class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("Email jest wymagany")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)

    def create_initial_user(self, email, **extra_fields):
        """
        Create and save a user with given email without password.
        """

        if not email:
            raise ValueError("Email jest wymagany")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        random_password = get_random_string(length=32)
        user.set_password(random_password)
        user.is_active = False
        user.save()
        return user

