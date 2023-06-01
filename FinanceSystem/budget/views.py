from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, Budget, Income
from .forms import BudgetCreationForm, ExpenseCreationForm

def budget_status(request):
    if Budget.objects.get(user=request.user):
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

def expense_creation(request):
    budget = Budget.objects.filter(user=request.user)
    form = ExpenseCreationForm()
    if request.method == 'POST':
        form = ExpenseCreationForm(request.post)
        if form.is_valid():
            form.owner = request.user
            form.save()

def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    return render(request, 'budget/expense_detail.html', {
        'expense':expense
    })

