from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    name = models.CharField(max_length=20)
#   dwa miejsca po przecinku
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, related_name='expense', on_delete=models.CASCADE)

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural= 'Expenses'
    # elementy tabeli zwracają swoją nazwe 

class Income(models.Model):
    name = models.CharField(max_length=20)
    income = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    money_owner = models.ForeignKey(User, related_name='income', on_delete=models.CASCADE)

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural= 'Expenses'
    # elementy tabeli zwracają swoją nazwe 



class Budget(models.Model):
    wealth = models.DecimalField(max_digits=12, decimal_places=2)
    weekly_limit = models.FloatField(max_length=9)

    user = models.OneToOneField(User, related_name='budget', on_delete=models.CASCADE)
    expenses = models.ManyToManyField(Expense, related_name='budgets')
    incomes = models.ManyToManyField(Income, related_name='budgets')


    class Meta:
        verbose_name_plural = 'Budgets'
    
    def __str__(self):
        return f"{self.user.username}'s Budget"
    
    def delete(self, *args, **kwargs):
        self.expenses.clear()
        self.incomes.clear()
        super().delete(*args, **kwargs)