from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from OSP_APP import settings
from accounts.views import Register, CustomLoginView, LogoutPageView, ActivationConfirmView, \
    ActivationCompleteView, UserPasswordChangeView, UserPasswordChangeDoneView, UserPasswordResetView, \
    UserPasswordResetDoneView, UserPasswordResetConfirmView, UserPasswordResetCompleteView, Home

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'), #TODO Zablokowanie wejscia osoba postronnym
    path('logout/', LogoutPageView.as_view(), name='logout'),
#     path('profile/', views.Profile.as_view(), name='profile'),
    path('activation/confirm/<uidb64>/<token>/', ActivationConfirmView.as_view(), name='activation_token_confirm'),
    path('activation/complete/', ActivationCompleteView.as_view(), name='activation_token_complete'),
    path('user/<int:pk>/password/change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('user/<int:pk>/password/change/done/', UserPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password/reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password/reset/done', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password/reset/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/complete/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
