# from django.db import models
# from django.contrib.auth import get_user_model
#
# UserModel = get_user_model()
#
#
# DRIVER_LICENSE_CHOICES = [
#     ('B', 'B'),
#     ('C', 'C'),
#     ('C+E', 'C+E'),
# ]
#
#
# class DriverLicense(models.Model):
#     category = models.CharField(choices=DRIVER_LICENSE_CHOICES, max_length=3)
#     permission_date = models.DateField()
#     emergency_permission_date = models.DateField()
#     user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
#
#
# class MedicalCheckup(models.Model):
#     date = models.DateField()
#     blood_type = models.CharField(max_length=3, null=True, blank=True)
#     user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
#
#
# class Training(models.Model):
#     training_name = models.CharField(max_length=100)
#     user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
#
#
# class SmokeBox(models.Model):
#     date = models.DateField()
#     user = models.OneToOneField(UserModel, on_delete=models.CASCADE)


# class Equipment(models.Model):
#     name = models.CharField(max_length=100)
#     expiration = models.DateField(null=True, blank=True)
#     amount = models.IntegerField(default=0)
#     # TODO: ewentualnie relacja z autem
#
#
# class Vehicle(models.Model):
#     name = models.CharField(max_length=100)
#     shortcut = models.CharField(max_length=100)
#     code_name = models.CharField(max_length=100)
#     license_category = models.CharField(choices=DRIVER_LICENSE_CHOICES, max_length=3)
#     inspection_date = models.DateField()
#     insurance_date = models.DateField()
#     # TODO: ewentualnie relacja z sprzętem
#
#     def __str__(self):
#         return self.shortcut
#
#
# class DepotTrip(models.Model):
#     date = models.DateField()
#     address = models.CharField(max_length=100)
#     dispatch_time = models.TimeField()
#     vehicles = models.ManyToManyField(Vehicle)
#     incident = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='depot_trips', null=True, blank=True)


