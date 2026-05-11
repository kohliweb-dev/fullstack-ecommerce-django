
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email =  request.POST['email']
        password = request.POST['password'] 
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request,'password didnot match')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'username already exists')
        else:
            User.objects.create_user(username=username,email=email,password=password)
            messages.success(request,'Account created , please login ')
            return redirect('login')
    return render(request,'signup.html')    

 
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credential')

    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html',{'user':request.user})

def logout_view(request):
    logout(request)
    return redirect('login')        

