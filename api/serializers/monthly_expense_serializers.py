from rest_framework import serializers

from api.models import MonthlyExpense


class MonthlyExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyExpense
        fields = ['id', 'created', 'cost', 'name']
        read_only_fields = ['id', 'created']
