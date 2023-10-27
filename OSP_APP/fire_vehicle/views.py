from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from fire_vehicle.models import FireVehicle


class GCBAView(ListView):
    model = FireVehicle
    template_name = 'fire_vehicle/gcba.html'
    context_object_name = 'firevehicle'

    def get_queryset(self):
        return FireVehicle.objects.get(code_name='649[S]43')
