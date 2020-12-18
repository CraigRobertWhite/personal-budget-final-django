from rest_framework import serializers

from api.models import AccountTransaction


class AccountTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountTransaction
        fields = ['id', 'created', 'amount', 'account']
        read_only_fields = ['id', 'created']
