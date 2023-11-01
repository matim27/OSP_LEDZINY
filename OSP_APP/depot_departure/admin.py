from django.contrib import admin

from depot_departure.models import DepotDeparture


@admin.register(DepotDeparture)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('trip_id', 'date', 'address', 'dispatch_time', 'incident', 'image')
