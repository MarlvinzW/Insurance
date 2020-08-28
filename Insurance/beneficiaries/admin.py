from django.contrib import admin
from .models import Beneficiary

"""
    BENEFICIARY MODEL ADMIN
"""


@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('guardian', 'first_name', 'last_name', 'phone_number', 'sex')
    list_per_page = 50
    search_fields = ('first_name', 'last_name', 'phone_number')
    fieldsets = (
        (None, {'fields': ('guardian',)}),
        ('Personal Info',
         {'fields': ('first_name', 'last_name', 'sex', 'date_of_birth', 'id_number', 'phone_number')
          }),
    )
    list_filter = ('date', 'time')
