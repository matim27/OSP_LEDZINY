from django.contrib import admin
from custom_auth.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'date_joined', 'is_superuser')


admin.site.register(User, UserAdmin)