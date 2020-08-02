from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def dash(request):
    return render(request, 'mainpage/dashboard.html')

def login(request):
    return render(request, 'mainpage/login.html')

def cli(request):
    return render(request, 'mainpage/clientes.html')

def jobs(request):
    return render(request, 'mainpage/trabajos.html')

def tags(request):
    return render(request, 'mainpage/categorias.html')
