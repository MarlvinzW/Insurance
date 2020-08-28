from django.contrib import admin
from django.conf import settings
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

admin.site.site_header = f'{settings.PLATFORM_NAME} Super Admin'
admin.site.site_title = 'Admin Portal'
admin.site.index_title = f'{settings.PLATFORM_NAME} Admin'


"""
    USER MODEL ADMIN
"""


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone_number', 'email')
    list_per_page = 50
    search_fields = ('email', 'username')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info',
         {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'id_number', 'address', 'province',
                     'nationality')
          }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'has_confirmed_email', 'password_reset'),
                         }),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_filter = ('date_joined', 'is_active', 'is_staff', 'is_superuser', 'has_confirmed_email')
