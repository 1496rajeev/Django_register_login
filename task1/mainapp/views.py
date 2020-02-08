from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login
from .models import Profile


# Create your views here.

def home(request):
    if request.method == "GET":
        return render(request, "home.html")

def register(request):
    if request.method == "GET":
        reg_form = RegisterForm()
        return render(request, "register.html",{"reg_form" : reg_form}) 

    elif request.method == "POST":
        reg_form = RegisterForm(request.POST)
        data = {i:request.POST.get(i).strip() for i in request.POST}

        if reg_form.is_valid() and len(data["password"])>=8:
        
            db_temp = reg_form.save(commit=False)
            db_temp.set_password(data["password"])
            db_temp.save()
            errors = "Successfully Registered"
            return render(request, "register.html", {"errors":errors})
        else:
            errors = reg_form.errors
            if len(data["password"])<8:
                errors = "Password must be 8 digit long"
            
            
            
            return render(request, "register.html", {"reg_form":reg_form, "errors" : errors})    
            
    

def loginfunc(request):
    if request.method == "GET":
        login_form = LoginForm()

        return render(request, 'login.html', {"login_form":login_form})

    if request.method == "POST":
        login_form = LoginForm()
        data = {key:request.POST.get(key) for key in request.POST}
        valid_user = authenticate(username = data["username"], password = data["password"])
        if valid_user is not None:
            if valid_user.is_active:
                login(request, valid_user)
                profile = Profile.objects.get(username=data["username"])
                return render(request, "successlogin.html", {'profile' : profile})
        else:
            errors="Not authentic user! Please check userame and password 1 more time."
            return render(request, 'login.html', {"errors":errors, "login_form":login_form})

        return render(request, template_name='login.html')

    
