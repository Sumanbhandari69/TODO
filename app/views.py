from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as loginuser
# from django.contrib import messages


def home(request):
    return render(request,'app/home.html')

def login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
        context ={
        "form":form
        }
        return render(request,'app/login.html', context=context)
    else:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # print("Authenticated", user)
            if user is not None:
                loginuser(request, user)
                return redirect('home')

        else:
            context ={
                "form":form
            }
            return render(request,'app/login.html', context=context)


def signup_view(request):
    if request.method=='GET':
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request,'app/signup.html', context= context)
    
    else:
        # print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
            "form" : form
        }
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
        else:
            # print(form.errors) 
            return render(request,'app/signup.html', context= context)
