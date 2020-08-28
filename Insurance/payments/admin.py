from django.contrib import admin
from .models import AccountBalance, CheckOut, PaynowConfig, Payment


"""
    PAYMENTS MODEL ADMIN
"""


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('reference', 'name', 'amount', 'has_paid')
    list_per_page = 50
    search_fields = ('reference', 'name', 'email')
    list_filter = ('has_paid', 'date', 'time')
    fieldsets = (
        ('Client Details',
         {'fields': ('name', 'email')
          }),
        ('Payment Details',
         {'fields': ('reference', 'amount', 'has_paid', 'payment_url', 'status_url')
          }),
    )


"""
    PAYNOW MODEL ADMIN
"""


@admin.register(PaynowConfig)
class PaynowConfigAdmin(admin.ModelAdmin):
    list_display = ('integration_key', 'integration_id')
    list_per_page = 10
    search_fields = ('integration_key', 'integration_id')
    fieldsets = (
        ('Integration ID',
         {'fields': ('integration_id',)
          }),
        ('Integration Key',
         {'fields': ('integration_key',)
          }),
    )

    MAX_OBJECTS = 1

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        if self.model.objects.count() >= 1:
            return False
        return super().has_delete_permission(request)


"""
    ACCOUNT BALANCE MODEL ADMIN
"""


@admin.register(AccountBalance)
class AccountBalanceAdmin(admin.ModelAdmin):
    list_display = ('holder', 'balance', 'last_paid')
    list_per_page = 50
    search_fields = ('holder', )
    fieldsets = (
        (None, {'fields': ('holder',)}),
        ('Payment Info',
         {'fields': ('balance', 'last_paid')
          })
    )
    list_filter = ('last_paid',)


"""
    CHECKOUT MODEL ADMIN
"""


@admin.register(CheckOut)
class CheckOutAdmin(admin.ModelAdmin):
    list_display = ('holder', 'beneficiary', 'amount', 'date', 'time')
    list_per_page = 50
    search_fields = ('holder', 'beneficiary')
    fieldsets = (
        (None, {'fields': ('holder', 'beneficiary')}),
        ('CheckOut Info',
         {'fields': ('amount', 'date', 'time')
          }),
    )
    list_filter = ('date', )
