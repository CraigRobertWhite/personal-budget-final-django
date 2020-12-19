from rest_framework import serializers

from api.models import Account, AccountTransaction


class AccountSerializer(serializers.ModelSerializer):
    from .account_transaction_serializers import AccountTransactionSerializer

    transactions = AccountTransactionSerializer(many=True, read_only=True)
    balance = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'created', 'name', 'transactions', 'balance']
        read_only_fields = ['id', 'created', 'transactions', 'balance']

    def get_balance(self, obj):
        try:
            return obj.transactions.latest().amount
        except AccountTransaction.DoesNotExist as e:
            return 0

    def create(self, validated_data):
        account = None
        account_transaction = None

        try:
            if user := self.context['request'].user:
                validated_data['user_id'] = user.id
            else:
                raise serializers.ValidationError('A user is required to create an account.')

            if not (amount := self.initial_data.get('amount')):
                raise serializers.ValidationError({
                    'amount': 'This field is required.'
                })

            account = super().create(validated_data)

            account_transaction_serializer = self.AccountTransactionSerializer(data={
                'amount': amount,
                'account': account.id
            })
            account_transaction_serializer.is_valid(raise_exception=True)
            account_transaction = account_transaction_serializer.save()

            return account
        except Exception as e:
            if account_transaction:
                account_transaction.delete()
            if account:
                account.delete()
            raise e
