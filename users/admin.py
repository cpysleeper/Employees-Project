
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_staff')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )

admin.site.register(User, CustomUserAdmin)