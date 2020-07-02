from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(request):
    return render(request, 'cuentas/dashboard.html')

def login(request):
    return render(request, 'cuentas/login.html')

def productos(request):
    return HttpResponse('productos')

def customer(request):
    return HttpResponse('customer')

