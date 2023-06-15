from rest_framework import serializers
from django.contrib.auth.models import User
from budget.models import Income, Expense, Budget


# lista użytkowników
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class BudgetSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Budget
        fields = ['id','wealth', 'weekly_limit', 'last_week_spent', 'user', 'expenses', 'incomes']

class IncomeSerializer(serializers.ModelSerializer):
    money_owner = UserSerializer()
    class Meta:
        model = Income
        fields = ['id', 'name', 'income', 'description', 'created_at', 'money_owner']

class ExpenseSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model = Expense
        fields = ['id', 'name', 'cost', 'description', 'created_at', 'owner']