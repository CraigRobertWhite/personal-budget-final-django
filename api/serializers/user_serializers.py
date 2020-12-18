from rest_framework import serializers

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'auth0_id', 'email', 'first_name', 'last_name']
        read_only_fields = ['id', 'auth0_id']
