from django.db import models

from .base_model import BaseModel


class Account(BaseModel):
    name = models.TextField()

    user = models.ForeignKey('User', related_name='accounts', on_delete=models.CASCADE)
