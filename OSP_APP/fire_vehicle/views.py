from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from depot_departure.models import DepotDeparture
from fire_vehicle.models import FireVehicle


class GCBAView(ListView):
    model = FireVehicle
    template_name = 'fire_vehicle/gcba.html'
    context_object_name = 'firevehicle'
    queryset = FireVehicle.objects.get(code_name='649[S]43')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicle_id = FireVehicle.objects.get(code_name='649[S]43')
        depot_count = DepotDeparture.objects.filter(vehicles=vehicle_id).count()
        context['depot_count'] = depot_count
        return context
