from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    # path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.LogoutPageView.as_view(), name='logout'),
    path('profile/', views.LawFirmProfile.as_view(), name='law_firm_profile'),

    path('activation/confirm/<uidb64>/<token>/', views.ActivationConfirmView.as_view(), name='activation_token_confirm'),
    path('activation/complete/', views.ActivationCompleteView.as_view(), name='activation_token_complete'),
    path('redirect', views.redirect_view, name='redirect'),

    path('customer/<int:pk>/password/change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('customer/<int:pk>/password/change/done/', views.UserPasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password/reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password/reset/done', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password/reset/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/complete/', views.UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)