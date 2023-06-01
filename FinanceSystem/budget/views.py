from django.shortcuts import render, redirect
from .models import Expense, Budget, Income
from .forms import BudgetCreationForm

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
        redirect('budget_creation')
    return render(request, 'budget/budget_status.html' ,context)

def budget_creation(request):
    form = BudgetCreationForm()
    if request.method == 'POST':
        form = BudgetCreationForm(request.post)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('budget/budget_status/')
        else:
            form = BudgetCreationForm()
    return render(request, 'budget/budget_creation.html',{
        'form' : form
    })
