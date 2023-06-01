from django.urls import path
from . import views

urlpatterns = [
    path('', views.budget_status, name='budget_status'),
    path('budget_creation', views.budget_creation, name='budget_creation'),
    # path('expense_detail/<int:pk>', views.expense_detail, name='expense_detail')
]
