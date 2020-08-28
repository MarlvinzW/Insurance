from django.db import models

from users.models import User

"""
    ACCOUNT BALANCE MODEL
"""


class AccountBalance(models.Model):
    holder = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account_holder')
    balance = models.FloatField(default=0)
    last_paid = models.DateTimeField()

    def __str__(self):
        return f'{self.holder.username} - ${self.balance}'

    class Meta:
        ordering = ['holder', 'balance']
        verbose_name_plural = 'Account Balances'
        verbose_name = 'Account Balance'


"""
    CHECKOUT MODEL
"""


class CheckOut(models.Model):
    holder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account_holder_checkout')
    beneficiary = models.ForeignKey(User, on_delete=models.CASCADE, related_name='beneficiary_checkout')
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.holder.username} => {self.beneficiary.first_name} - ${self.amount}'

    class Meta:
        ordering = ['date', 'time']
        verbose_name_plural = 'CheckOuts'
        verbose_name = 'CheckOut'


"""
    PAYNOW CONFIG MODEL
"""


class PaynowConfig(models.Model):
    integration_id = models.CharField(max_length=4)
    integration_key = models.CharField(max_length=38)

    def __str__(self):
        return f'Paynow Details {self.integration_id}'

    class Meta:
        verbose_name_plural = 'Paynow Details'
        verbose_name = 'Paynow Details'


"""
    PAYMENT MODEL
"""


class Payment(models.Model):
    reference = models.CharField(max_length=255, unique=True)
    payee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='beneficiary_payment')
    amount = models.FloatField()
    has_paid = models.BooleanField(default=False)
    payment_url = models.URLField()
    status_url = models.URLField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.reference + ' - $' + str(self.amount) + ' ' + str(self.payee.username)

    class Meta:
        verbose_name_plural = 'Payments'
        verbose_name = 'Payment'
        ordering = ['date', 'time']
