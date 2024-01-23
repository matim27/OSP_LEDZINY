from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from depot_tips.models import DepotTip, TipsImage


# Create your views here.

class DepotTipsView(ListView):
    model = DepotTip
    template_name = 'depot_tips/depot_tip_list.html'
    context_object_name = 'depot_tips'

    def is_member_of_group(self):
        return self.request.user.groups.filter(name='Depot_departure_add').exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_member'] = self.is_member_of_group()
        return context


class DepotTipAddView(CreateView):
    model = DepotTip
    template_name = 'depot_tips/depot_tip_add.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('depot_tips')


class DepotTipImageAddView(CreateView):
    model = TipsImage
    template_name = 'depot_tips/depot_tip_image_add.html'
    fields = ['image', 'depot_tip']
    success_url = reverse_lazy('depot_tips')
