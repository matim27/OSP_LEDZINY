from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from depot_departure.models import DepotDeparture
from fire_vehicle.models import FireVehicle


UserModel = get_user_model()

class DepotDepartureForm(forms.ModelForm):
    vehicles = forms.ModelMultipleChoiceField(
        queryset=FireVehicle.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Pojazdy uczestniczace w wyjezdzie',
    )
    manning = forms.ModelMultipleChoiceField(
        queryset=UserModel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Obsada na wyjezdzie',
    )

    class Meta:
        model = DepotDeparture
        fields = ['date', 'address', 'dispatch_time', 'vehicles', 'incident', 'image', 'manning']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'dispatch_time': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'trip_id': 'Numer wyjazdu || np. 001/2023',
            'date': 'Data wyjazdu',
            'address': 'Adres Zdarzenia',
            'dispatch_time': 'Godzina wyjazdu',
            'incident': 'Rodzaj zdarzenia',
            'image': 'Zdjecie',
        }
