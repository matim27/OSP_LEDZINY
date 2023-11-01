from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import UserForm
from custom_auth.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    search_fields = ('email', 'first_name', 'last_name', 'phone_number')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Dane Osobowe', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permisje', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Daty', {'fields': ('last_login', 'date_joined')}),
        ('Uprawnienia', {'fields': ('groups', 'user_permissions')}),
    )
    add_form = UserForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name'),
        }),
    )
    ordering = ('email',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.send_email_to_new_user(request)


admin.site.register(User, CustomUserAdmin)
