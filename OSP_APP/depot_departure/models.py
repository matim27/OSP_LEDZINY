from django.contrib.auth import get_user_model
from django.db import models
from fire_vehicle.models import FireVehicle
from django.contrib.auth.models import User


UserModel = get_user_model()

class DepotDeparture(models.Model):
    trip_id = models.CharField(max_length=10, unique=True, blank=True)
    date = models.DateField()
    address = models.CharField(max_length=150)
    dispatch_time = models.TimeField()
    vehicles = models.ManyToManyField(FireVehicle)
    incident = models.CharField(max_length=225)
    image = models.ImageField(upload_to='depot_departure_images', null=True, blank=True)
    manning = models.ManyToManyField(UserModel, blank=True)

    def save(self, *args, **kwargs):
        if not self.trip_id:
            year = self.date.year
            last_trip_in_year = DepotDeparture.objects.filter(date__year=year).order_by('-trip_id').first()
            if last_trip_in_year:
                last_trip_id, last_trip_year = last_trip_in_year.trip_id.split('/')
                if int(last_trip_year) == year:
                    trip_id = str(int(last_trip_id) + 1).zfill(3)
                else:
                    trip_id = '001'
            else:
                trip_id = '001'
            self.trip_id = f'{trip_id}/{year}'
            self.year = year
        super().save(*args, **kwargs)
    def __str__(self):
        return f'Wyjazd {self.trip_id}'
