from django.shortcuts import render , redirect
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from users_app.forms import CustomRegisterationForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == "POST":
        register_form = CustomRegisterationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request , ("Registered Successfully! You can now login"))
            return redirect('register')    
    else:    
        register_form = CustomRegisterationForm()
    return render(request,'users/register.html',{'register_form':register_form})