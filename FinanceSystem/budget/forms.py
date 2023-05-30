from django import forms
from .models import Budget

class BudgetCreationForm(forms.ModelForm):
    wealth = forms.CharField(min_length=3, max_length=12, widget=forms.NumberInput(attrs={
        'placeholder':'Your wealth',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    weekly_limit = forms.CharField(min_length=3, max_length=12, widget=forms.NumberInput(attrs={
        'placeholder':'Weekly limit',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))     
    user = ...
    
    class Meta:
        model = Budget