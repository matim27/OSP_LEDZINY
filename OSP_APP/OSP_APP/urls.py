from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('accounts.urls')),
    path('', include('account_details.urls')),
    path('', include('fire_vehicle.urls')),
    path('', include('depot_departure.urls')),
]
