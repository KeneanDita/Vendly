from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm , AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 px-6 rounded-xl bg-white'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Password',
        'class': 'w-full py-4 px-6 rounded-xl bg-white'
    }))
    
    
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Username',
        'class': 'w-full py-4 px-6 rounded-xl bg-white'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Email',
        'class': 'w-full py-4 px-6 rounded-xl bg-white'
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter a Password',
        'class': 'w-full py-4 px-6 rounded-xl bg-white'
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Cpnfirm Your Password',
        'class': 'w-full py-4 px-6 rounded-xl bg-white'
    }))