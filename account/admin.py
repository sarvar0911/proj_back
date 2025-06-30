from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'is_active']

    fieldsets = (
        (None, {'fields': ('username', 'is_active', 'is_staff', 'password')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )


admin.site.unregister(Group)
