from django.shortcuts import render , redirect
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from users_app.forms import CustomRegisterationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView

# Create your views here.

def register(request):
    """The function recives register POST request from the user
    and validates wih the help of django registeration form
    library"""

    if request.method == "POST":
        register_form = CustomRegisterationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request , ("Registered Successfully! You can now login"))
            return redirect('register')    
    else:   
        register_form = CustomRegisterationForm()
    return render(request,'users/register.html',{'register_form':register_form})





class LoginView(LoginView):

    """ WE are overriding the login method
    as by default if you enter wrong login details
    response code is 200
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 401
        return response