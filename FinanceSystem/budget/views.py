from django.shortcuts import render
from .models import Expense, Budget, Income

def budget_status(request):
    budget = Budget.objects.filter(user=request.user)
    expenses = Expense.objects.filter(created_by=budget.user.username)
    incomes = Income.objects.filter(created_by=budget.user.username)
    context = {
        'expenses':expenses,
        'budget':budget,
        'incomes':incomes
    }
    return render(request, context)


