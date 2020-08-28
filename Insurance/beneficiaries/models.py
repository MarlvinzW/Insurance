from django.db import models

import constants
from users.models import User

"""
    BENEFICIARY MODEL
"""


class Beneficiary(models.Model):
    guardian = models.ForeignKey(User, on_delete=models.CASCADE, related_name='beneficiary_guardian')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=10, choices=constants.sex)
    phone_number = models.CharField(max_length=20, help_text='eg 263775580596')
    id_number = models.CharField(max_length=14, help_text='eg 00-000000-A00')
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} - {self.guardian.username}'

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Beneficiary'
        verbose_name_plural = 'Beneficiaries'
