from django.db import models

from .base_model import BaseModel


class Goal(BaseModel):
    amount = models.IntegerField()
    name = models.TextField()

    user = models.ForeignKey('User', related_name='goals', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'user'], name='unique_user_goals')
        ]
