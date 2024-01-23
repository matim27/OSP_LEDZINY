from django.contrib import admin

from depot_tips.models import DepotTip, TipsImage


# Register your models here.
@admin.register(DepotTip)
class DepotTipAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(TipsImage)
class TipsImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'depot_tip')