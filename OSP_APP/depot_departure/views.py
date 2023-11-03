from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from depot_departure.forms import DepotDepartureForm
from depot_departure.models import DepotDeparture


class DepotDepartureAddView(CreateView):
    template_name = 'depot_departure/add/depot_departure_add.html'
    model = DepotDeparture
    form_class = DepotDepartureForm
    success_url = reverse_lazy('home')


class DepotDepartureListView(ListView):
    model = DepotDeparture
    template_name = 'depot_departure/list/depot_departure_list.html'
    context_object_name = 'depot'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_depot_departure = DepotDeparture.objects.order_by('-trip_id')
        context['last_depot'] = last_depot_departure
        return context
