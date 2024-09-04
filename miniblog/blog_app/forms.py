from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Blog

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password(again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}), 'email': forms.EmailInput(attrs={'class': 'form-control'}), 'first_name': forms.TextInput(attrs={'class': 'form-control'}), 'last_name': forms.TextInput(attrs={'class': 'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog 
        fields = ['title', 'author', 'body']
        labels = {'title':'Title', 'author':'Author', 'body':'Body'}
        widgets = {'title': forms.TextInput(attrs={'class':'form-control'}), 'author': forms.TextInput(attrs={'class':'form-control'}), 'body': forms.Textarea(attrs={'class':'form-control'})}
