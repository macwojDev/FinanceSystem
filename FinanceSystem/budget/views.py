from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, Budget, Income
from .forms import BudgetCreationForm, ExpenseCreationForm, IncomeCreationForm

# widok budżetu, centralnej części aplikacji
def budget_status(request):
    budget_exists = Budget.objects.filter(user=request.user).exists()
# pobieranie ustalonego limitu tygodniowego
    if 'limit' in request.GET.get:
        limit = request.GET.get('limit')
        limit = float(limit)
        budget.weekly_limit = limit
        budget.save()
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
#   przekierowanie do formularza utworzenia budżetu, w momencie gdy użytkownik go nie posiada
    else:
        return redirect('budget_creation')
    
# utworzenie budżetu
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

# Widoki dodawania zmian w budżecie 
def new_expense(request):
    budget = Budget.objects.get(user=request.user)
    form = ExpenseCreationForm()
    if request.method == 'POST':
        form = ExpenseCreationForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.owner = request.user
            expense.save()
            budget.wealth = float(budget.wealth)
            budget.wealth -= float(expense.cost)
            budget.expenses.add(expense)
            budget.save()
            return redirect('budget_status')
        else:
            form = ExpenseCreationForm()
    return render(request, 'budget/forms.html',{
        'form':form
    })

def new_income(request):
    budget = Budget.objects.get(user=request.user)
    form = IncomeCreationForm()
    if request.method == 'POST':
        form = IncomeCreationForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.money_owner = request.user
            income.save()
            budget.wealth = float(budget.wealth)
            budget.wealth += float(income.income)
            budget.incomes.add(income)
            budget.save()
            return redirect('budget_status')
        else:
            form = IncomeCreationForm()
    return render(request, 'budget/forms.html', {
        'form':form
    })


def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    return render(request, 'budget/expense_detail.html', {
        'expense':expense
    })
def income_detail(request, pk):
    income = get_object_or_404(Income, pk=pk)
    return render(request, 'budget/income_detail.html', {
        'income':income
    })

def income_delete(request, pk):
    expense = get_object_or_404(Expense,pk=pk)
    budget = Budget.objects.get(user = request.user)
    budget.wealth = float(budget.wealth)
    budget.wealth += float(expense.cost)
    budget.save()
    expense.delete()
    return redirect('budget_status')

def income_delete(request, pk):
    income = get_object_or_404(Income,pk=pk)
    budget = Budget.objects.get(user = request.user)
    budget.wealth = float(budget.wealth)
    budget.wealth -= float(income.income)
    budget.save()
    income.delete()
    return redirect('budget_status')

