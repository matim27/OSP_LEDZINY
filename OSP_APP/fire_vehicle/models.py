from django.db import models


DRIVER_LICENSE_CHOICES = [
    ('B', 'B'),
    ('C', 'C'),
    ('C+E', 'C+E'),
]


class FireVehicle(models.Model):
    name = models.CharField(max_length=100)
    shortcut = models.CharField(max_length=100)
    code_name = models.CharField(max_length=100)
    license_category = models.CharField(choices=DRIVER_LICENSE_CHOICES, max_length=3)
    inspection_date = models.DateField(blank=True, null=True)
    insurance_date = models.DateField(blank=True, null=True)
    # TODO: ewentualnie relacja z sprzętem

    def __str__(self):
        return self.shortcut
