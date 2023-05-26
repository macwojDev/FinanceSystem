from django.urls import path
from . import views

urlpatterns = [
    path('', views.budget_status, name='budget_status')
]
