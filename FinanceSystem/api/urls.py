from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('budgets/', views.BudgetList.as_view()),
    path('incomes/', views.IncomeList.as_view()),
    path('expenses/', views.ExpenseList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)