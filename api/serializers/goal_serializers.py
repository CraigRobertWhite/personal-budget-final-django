from rest_framework import serializers

from api.models import Goal


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'created', 'amount', 'name']
        read_only_fields = ['id', 'created']

    def create(self, validated_data):
        if user := self.context['request'].user:
            validated_data['user_id'] = user.id
        else:
            raise serializers.ValidationError('A user is required to create an account.')
        return super().create(validated_data)
