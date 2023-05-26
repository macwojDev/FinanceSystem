from django.shortcuts import render, redirect
from .forms import SignupForm
# from django.contrib.auth.views import LoginView, LogoutView

def index(request):
    return render(request, 'core/index.html')

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            form = SignupForm()

    return render(request, 'core/signup.html',{
        'form' : form
    })
    

'''
class Logowanie(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        remember_me = self.request.POST.get('remember_me')
        if remember_me == 'true':
            response.set_cookie('remember_me', True, max_age=3600*24*7)
            response.set_cookie('username', form.cleaned_data['username'])
            response.set_cookie('login_status', True)
        return response
    
class Wylogowanie(LogoutView):

    def dispatch(self, request):
        response = super().dispatch(request)

        response.delete_cookie('username')
        response.delete_cookie('login_status')
        response.delete_cookie('remember_me')
        return response
'''