from django.shortcuts import render,redirect
from django.http import HttpResponse


def home(request):
    pass

def cadastro(request):
    pass


def login(request):
    return render(request,'login.html')


def logout(request):
    pass