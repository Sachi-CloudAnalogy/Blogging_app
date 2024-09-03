from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Blog

#Home
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

#About
def about(request):
    return render(request, 'about.html')

#Contact
def contact(request):
    return render(request, 'contact.html')

#Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.all()
        return render(request, 'dashboard.html', {'blogs': blogs})
    else:
        return HttpResponseRedirect('/login/')

#sign up
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations !! You have become an Author')
            form.save()
        else:
            print(form.errors)
    else:    
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

#login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/dashboard/')
        else:        
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')

#logout
def user_logout(request):
   logout(request)
   return HttpResponseRedirect('/')

#add new post
def add_blog(request):
    if not request.user.is_authenticated:
        return render(request, 'addblog.html')
    else:
        return HttpResponseRedirect('/login/')

#update post
def update_blog(request):
    if not request.user.is_authenticated:
        return render(request, 'updateblog.html')
    else:
        return HttpResponseRedirect('/login/')