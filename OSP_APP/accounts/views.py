from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import INTERNAL_RESET_SESSION_TOKEN, PasswordResetConfirmView, PasswordResetCompleteView, \
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View, generic
from .forms import UserForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login


UserModel = get_user_model()


class Home(generic.TemplateView):
    template_name = 'home.html'


class Register(generic.CreateView):
    template_name = 'login/user_register.html'
    form_class = UserForm

    def form_valid(self, form):
        """If the form is valid, save the associated model and send email."""
        # user = form.save()
        # user.send_email_to_new_user(self.request)
        # return super().form_valid(form)
        response = super().form_valid(form)
        self.object.save()
        self.object.send_email_to_new_user(self.request)
        return response


class ActivationConfirmView(PasswordResetConfirmView):
    template_name = 'profile_activation/activation_confirm.html'
    success_url = reverse_lazy('activation_token_complete')

    def form_valid(self, form):
        user = form.save()
        user.is_active = True
        user.save()
        del self.request.session[INTERNAL_RESET_SESSION_TOKEN]
        if self.post_reset_login:
            auth_login(self.request, user, self.post_reset_login_backend)
        return HttpResponseRedirect(self.get_success_url())


class ActivationCompleteView(PasswordResetCompleteView):
    form_class = SetPasswordForm
    template_name = 'profile_activation/activation_complete.html'


# class Profile(LoginRequiredMixin, generic.DetailView):
#     model = LawFirm
#     form_class = LawFirmForm
#     template_name = 'management/profile.html'
#
#     def get_object(self, queryset=None):
#         return self.request.user.profile.law_firm


class CustomLoginView(SuccessMessageMixin, LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login/user_login.html'
    success_url = reverse_lazy("home")
    success_message = "Zalogowano"


class LogoutPageView(LogoutView):
    pass


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'login/user_change_password.html'
    form_class = PasswordChangeForm

    def get_success_url(self):
        return reverse("login")


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    """Password has been changed"""
    template_name = 'login/user_change_password_done.html'


class UserPasswordResetView(PasswordResetView):
    """Start reset process"""
    form_class = PasswordResetForm
    template_name = 'login/user_reset_password.html'
    success_url = reverse_lazy('password_reset_done')
    html_email_template_name = 'emails/user_reset_password_email_new.html'


class UserPasswordResetDoneView(PasswordResetDoneView):
    """Instruction send"""
    template_name = 'login/user_reset_password_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    """Enter new password"""
    template_name = 'login/user_reset_password_confirm.html'
    success_url = reverse_lazy('password_reset_complete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    """Password changed"""
    form_class = SetPasswordForm
    template_name = 'login/user_reset_password_complete.html'
