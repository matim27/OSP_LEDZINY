from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from depot_departure.forms import DepotDepartureForm
from depot_departure.models import DepotDeparture


class DepotDepartureAddView(CreateView):
    template_name = 'depot_departure/add/depot_departure_add.html'
    model = DepotDeparture
    form_class = DepotDepartureForm
    success_url = reverse_lazy('home')
