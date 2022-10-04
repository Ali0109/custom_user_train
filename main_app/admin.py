from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from main_app.forms import *
from main_app.models import *


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'name',
        'password',
        'last_login',
        'is_superuser',
        'is_staff',
    ]
