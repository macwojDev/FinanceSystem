from django.shortcuts import render
from .models import Expenses, Budget

def budget(request):
    budget = Budget.objects.filter(user=request.user)
    expenses = Expenses.objects.filter(created_by=budget.user.username)
    context = {
        'expenses':expenses,
        'budget':budget
    }
    return render(request, context)


