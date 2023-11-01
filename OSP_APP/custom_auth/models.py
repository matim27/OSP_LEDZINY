from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.template.loader import get_template
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from custom_auth.managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    phone_number = PhoneNumberField(region='PL', null=True, blank=True)
    username = models.CharField(max_length=255, unique=False, blank=True, null=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Użytkownik'
        verbose_name_plural = 'Użytkownicy'


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    def send_email_to_new_user(self, request):

        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(self)
        subject = 'Ustaw hasło dla swojego konta w OSP Lędziny'
        from_email = settings.EMAIL_HOST_USER
        to_email = self.email
        html_template = get_template('emails/email_to_new_user.html')
        context = {
            'user': self,
            'domain': request.META['HTTP_HOST'],
            'uid': urlsafe_base64_encode(force_bytes(self.pk)),
            'token': token,
            'link': f"/activation/confirm/{urlsafe_base64_encode(force_bytes(self.pk))}/{token}",
            'protocol': 'http'
        }
        text_content = 'Ustaw hasło dla swojego nowego w OSP_APP'
        html_content = html_template.render(context)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)

    def get_absolute_url(self):
        return reverse('register')

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
