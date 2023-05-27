from django.shortcuts import render
from .models import Expense, Budget, Income

def budget_status(request):
    if Budget.objects.filter(user=request.user):
        budget = Budget.objects.filter(user=request.user)
        expenses = Expense.objects.filter(created_by=budget.user.username)
        incomes = Income.objects.filter(created_by=budget.user.username)
        context = {
            'expenses':expenses,
            'budget':budget,
            'incomes':incomes
    }
    else:
        render(request,'budget/budget_creation.html')
    return render(request, 'budget/budget_status.html' ,context)

def budget_creation(request):
    ...
