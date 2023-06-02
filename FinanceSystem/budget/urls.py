from django.urls import path
from . import views

urlpatterns = [
    path('budget_status/', views.budget_status, name='budget_status'),
    path('budget_creation/', views.budget_creation, name='budget_creation'),
    path('new_expense/', views.new_expense, name='new_expense')
    # path('expense_detail/<int:pk>', views.expense_detail, name='expense_detail')
]
