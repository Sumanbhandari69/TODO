from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse('Hello, World TO DO app')
    return render(request,'app/home.html')