from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms


class Signupform(UserCreationForm):
    username = forms.CharField(required = True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(required = True, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(required = True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ['username','first_name','email','password1']