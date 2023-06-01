from django import forms
from .models import Budget

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
    
    
    
    

