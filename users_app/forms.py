from enum import unique
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime





class CustomRegisterationForm(UserCreationForm, forms.Form):

    
    email = forms.EmailField( label='Email')
    first_name = forms.CharField(max_length=64,label='First Name')
    last_name = forms.CharField(max_length=64,label='Last Name')
    class Meta:
        model = User
        fields = ['username' , 'email', 'password1' , 'password2','first_name','last_name']