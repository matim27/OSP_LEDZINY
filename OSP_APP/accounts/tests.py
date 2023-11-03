import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import RequestFactory
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView
from django.core import mail

User = get_user_model()

@pytest.mark.django_db
def test_home_view(client, user):
    response = client.get(reverse('home'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_register_view(client):
    response = client.get(reverse('register'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_activation_confirm_view(client, user):
    # Przygotowanie danych dla testu
    token = default_token_generator.make_token(user)
    uid = user.pk

    response = client.get(reverse('activation_confirm', kwargs={'uidb64': uid, 'token': token}))
    assert response.status_code == 200

@pytest.mark.django_db
def test_login_view(client):
    response = client.get(reverse('login'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_logout_view(client):
    response = client.get(reverse('logout'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_user_password_change_view(client, user):
    # Zaloguj użytkownika
    client.force_login(user)
    response = client.get(reverse('user_password_change'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_user_password_reset_view(client):
    response = client.get(reverse('user_password_reset'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_user_password_reset_done_view(client):
    response = client.get(reverse('password_reset_done'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_user_password_reset_confirm_view(client, user):
    # Przygotowanie danych dla testu
    uid = user.pk
    token = default_token_generator.make_token(user)

    response = client.get(reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token}))
    assert response.status_code == 200

@pytest.mark.django_db
def test_user_password_reset_complete_view(client):
    response = client.get(reverse('password_reset_complete'))
    assert response.status_code == 200
