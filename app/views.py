from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as loginuser, logout
from app.forms import TODOForm
from app.models import TODO
from django.contrib.auth.decorators import login_required
# from django.contrib import messages

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('-priority')
        return render(request,'app/home.html', context = {'form' : form, 'todos' : todos})

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
        

@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        # print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')
        else:
            form = TODOForm()
        return render(request,'app/home.html', context = {'form' : form})
    
def signout(request):
    logout(request)
    return redirect('login')

def delete_todo(request, id):
    TODO.objects.get(pk=id).delete()
    return redirect('home')

def change_status(request, id, status):
    todo = TODO.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('home')


