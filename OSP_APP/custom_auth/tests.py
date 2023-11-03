import pytest
from django.contrib.auth import get_user_model
from .models import CustomUserManager

User = get_user_model()

@pytest.mark.django_db
def test_create_user():
    manager = CustomUserManager()
    user = manager.create_user(email="test@example.com", password="testpassword")
    assert user.email == "test@example.com"
    assert user.is_active is True
    assert user.is_staff is False
    assert user.is_superuser is False

@pytest.mark.django_db
def test_create_superuser():
    manager = CustomUserManager()
    user = manager.create_superuser(email="admin@example.com", password="adminpassword")
    assert user.email == "admin@example.com"
    assert user.is_active is True
    assert user.is_staff is True
    assert user.is_superuser is True

@pytest.mark.django_db
def test_create_initial_user():
    manager = CustomUserManager()
    user = manager.create_initial_user(email="new@example.com")
    assert user.email == "new@example.com"
    assert user.is_active is False
    assert user.check_password("")

