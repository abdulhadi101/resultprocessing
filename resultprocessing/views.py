from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

def homepage(request):
    context = {}

    return render (request, 'index.html', context)

def contactView(request):
    context = {}

    return render (request, 'contact.html', context)


def detailView(request):
    context = {}

    return render (request, 'detail.html', context)

