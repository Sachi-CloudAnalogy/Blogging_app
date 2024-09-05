from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm, BlogForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Blog
from django.contrib.auth.models import Group

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
        if request.user.is_superuser:
            blogs = Blog.objects.all()
        else:    
            blogs = Blog.objects.filter(author=request.user.get_full_name())
        user = request.user
        full_name = user.get_full_name()
        email = user.email
        group = user.groups.all()
        return render(request, 'dashboard.html', {'blogs': blogs, 'full_name': full_name, 'email': email, 'groups': group})
    else:
        return HttpResponseRedirect('/login/')

#sign up
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Blogger')
            user.groups.add(group)
            messages.success(request, 'Congratulations !! You have become a Blogger')
            return HttpResponseRedirect('/login/')
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
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                author = form.cleaned_data['author']
                body = form.cleaned_data['body']
                blog = Blog(title=title, author=author, body=body)
                blog.save()
                #form = BlogForm()
                return HttpResponseRedirect('/dashboard/')
        else:
            form = BlogForm()        
        return render(request, 'addblog.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')

#update post
def update_blog(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            blog = Blog.objects.get(pk=id)
            form = BlogForm(request.POST, instance=blog)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            blog = Blog.objects.get(pk=id)
            form = BlogForm(instance=blog)        
        return render(request, 'updateblog.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')
    
#Delete post
def delete_blog(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            blog = Blog.objects.get(pk=id)
            blog.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')   
     