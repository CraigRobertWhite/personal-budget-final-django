from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .base_model import BaseModel


class AccountTransaction(BaseModel):
    amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000000000)])

    account = models.ForeignKey('Account', related_name='transactions', on_delete=models.CASCADE)
