from django.contrib import admin

from account_details.models import SmokeBox, DriverLicense, MedicalCheckup, Training


@admin.register(DriverLicense)
class DriverLicenseAdmin(admin.ModelAdmin):
    list_display = ('category', 'permission_date', 'emergency_permission_date', 'user')


@admin.register(MedicalCheckup)
class MedicalCheckupAdmin(admin.ModelAdmin):
    list_display = ('date', 'blood_type', 'user')


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('training_name', 'user')


@admin.register(SmokeBox)
class SmokeBoxAdmin(admin.ModelAdmin):
    list_display = ('date', 'user')

