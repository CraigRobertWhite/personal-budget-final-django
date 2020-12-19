from django.db import models

from .base_model import BaseModel


class MonthlyExpense(BaseModel):
    cost = models.IntegerField()
    name = models.TextField()

    user = models.ForeignKey('User', related_name='monthly_expenses', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'user'], name='unique_user_expenses')
        ]
