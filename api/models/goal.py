from django.db import models

from .base_model import BaseModel


class Goal(BaseModel):
    amount = models.IntegerField()
    name = models.TextField()

    user_id = models.ForeignKey('User', related_name='goals', on_delete=models.CASCADE)
