from django.db import models
from django.contrib.auth.models import User

class Expenses(models.Model):
    name = models.CharField(max_length=40)
#   dwa miejsca po przecinku
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null = True)
    buyer = models.ForeignKey(User, related_name='expenses', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at")
        verbose_name_plural= 'Expenses'
    # elementy tabeli zwracają swoją nazwe 

class Budget(models.Model):
    user = models.ForeignKey(User, related_name='budget', on_delete=models.CASCADE, unique=True)
    expenses = models.ForeignKey(Expenses, related_name='budget', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Budget'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.verbose_name_plural = f"{self.user.username}'s Budgets"