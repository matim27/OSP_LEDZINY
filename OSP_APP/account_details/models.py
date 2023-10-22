from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


DRIVER_LICENSE_CHOICES = [
    ('B', 'B'),
    ('C', 'C'),
    ('C+E', 'C+E'),
]


class DriverLicense(models.Model):
    category = models.CharField(choices=DRIVER_LICENSE_CHOICES, max_length=3)
    permission_date = models.DateField(blank=True, null=True)
    emergency_permission_date = models.DateField(blank=True, null=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)


class MedicalCheckup(models.Model):
    date = models.DateField(blank=True, null=True)
    blood_type = models.CharField(max_length=3, blank=True, null=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)


class Training(models.Model):
    training_name = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.training_name


class SmokeBox(models.Model):
    date = models.DateField(blank=True, null=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)

