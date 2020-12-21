from rest_framework import serializers

from api.models import User, AccountTransaction


class UserSerializer(serializers.ModelSerializer):
    from .account_serializers import AccountSerializer
    from .monthly_expense_serializers import MonthlyExpenseSerializer
    from .goal_serializers import GoalSerializer

    accounts = AccountSerializer(many=True, read_only=True)
    monthly_expenses = MonthlyExpenseSerializer(many=True, read_only=True)
    goals = GoalSerializer(many=True, read_only=True)

    net_worth = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'auth0_id', 'email', 'first_name', 'last_name', 'accounts', 'monthly_expenses',
                  'monthly_gross_income', 'goals', 'net_worth', 'finished_registration']
        read_only_fields = ['id', 'auth0_id', 'accounts', 'monthly_expenses', 'goals']

    def get_net_worth(self, obj):
        net_worth = 0
        for account in obj.accounts.all():
            try:
                net_worth += account.transactions.latest().amount
            except AccountTransaction.DoesNotExist as e:
                pass
        return net_worth
