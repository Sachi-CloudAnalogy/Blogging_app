from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm

#Home
def home(request):
    return render(request, 'home.html')

#About
def about(request):
    return render(request, 'about.html')

#Contact
def contact(request):
    return render(request, 'contact.html')

#Dashboard
def dashboard(request):
    return render(request, 'dashboard.html')

#sign up
def signup(request):
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

#login
def login(request):
    return render(request, 'login.html')

#logout
def logout(request):
   return HttpResponseRedirect('/')
