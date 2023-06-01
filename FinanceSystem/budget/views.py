from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, Budget, Income
from .forms import BudgetCreationForm, ExpenseCreationForm

def budget_status(request):
    budget_exists = Budget.objects.filter(user=request.user).exists()
    if budget_exists:
        budget = Budget.objects.get(user=request.user)
        expenses = budget.expenses.all()
        incomes = budget.incomes.all()
        context = {
            'expenses':expenses,
            'budget':budget,
            'incomes':incomes
        }   
        return render(request, 'budget/budget_status.html' ,context)
    else:
        return redirect('budget_creation')
    

def budget_creation(request):
    form = BudgetCreationForm()
    if request.method == 'POST':
        form = BudgetCreationForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('budget_status')
        else:
            form = BudgetCreationForm()
    return render(request, 'budget/budget_creation.html',{
        'form' : form
    })

def expense_creation(request):
    budget = Budget.objects.filter(user=request.user)
    form = ExpenseCreationForm()
    if request.method == 'POST':
        form = ExpenseCreationForm(request.POST)
        if form.is_valid():
            form.owner = request.user
            form.save()

def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    return render(request, 'budget/expense_detail.html', {
        'expense':expense
    })

