from rest_framework import serializers

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    from .account_serializers import AccountSerializer

    accounts = AccountSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'auth0_id', 'email', 'first_name', 'last_name', 'accounts', 'monthly_gross_income']
        read_only_fields = ['id', 'auth0_id', 'accounts']
