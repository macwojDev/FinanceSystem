from django import forms
from .models import Budget, Expense, Income

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl'

class BudgetCreationForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ('wealth', 'weekly_limit')
        
        widgets = {
            'wealth' : forms.NumberInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'weekly_limit':forms.NumberInput(attrs={
                'class' : INPUT_CLASSES
            })
        }
        labels = {
            'wealth':'Your wealth',
            'weekly_limit':'Control your expenses with weekly limit!'
        }
    
class ExpenseCreationForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('name', 'cost', 'description')
        
        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'cost':forms.NumberInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'description' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            }),
        }
        labels = {
            'name':'Expense Name',
            'cost':'How much was it?',
            'description':'Describe the expense!'
        }
class IncomeCreationForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('name', 'income', 'description')
        
        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'income':forms.NumberInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'description' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            }),
        }
        labels = {
            'name':'Income Name',
            'income':'How much did you earn?',
            'description':'Describe the income!'
        }
    
    
    
    

