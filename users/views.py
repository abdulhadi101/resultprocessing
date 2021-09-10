from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

def userRegistration(request):
    
    return render (request, 'users/register.html', context)

def userLogin(request):
    context = {}
    return render(request, 'users/login.html', context)

