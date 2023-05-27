from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm


urlpatterns = [
    path('',views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name='logout')
]
