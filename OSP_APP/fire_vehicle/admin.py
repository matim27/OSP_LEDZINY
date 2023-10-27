from django.contrib import admin
from .models import FireVehicle


@admin.register(FireVehicle)
class FireVehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortcut', 'code_name', 'license_category', 'inspection_date', 'insurance_date')
