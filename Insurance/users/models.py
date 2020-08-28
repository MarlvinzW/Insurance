from django.db import models
from django.contrib.auth.models import AbstractUser
import constants

"""
    USER MODEL ADMIN
"""


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, help_text='eg 263775580596')
    id_number = models.CharField(max_length=14, help_text='eg 00-000000-A00')
    has_confirmed_email = models.BooleanField(default=False)
    address = models.CharField(max_length=255)
    province = models.CharField(max_length=255, choices=constants.provinces)
    nationality = models.CharField(max_length=200, choices=constants.counties)

    class Meta:
        verbose_name_plural = 'Users'
        ordering = ['username']

    def __str__(self):
        return self.username
