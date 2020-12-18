from django.db import models

from .base_model import BaseModel


class BankAccount(BaseModel):
    balance = models.IntegerField()
    name = models.TextField()

    user_id = models.ForeignKey('User', related_name='bank_accounts', on_delete=models.CASCADE)
