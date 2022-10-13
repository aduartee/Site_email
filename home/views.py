from django.shortcuts import render
from django.http import HttpResponse

def entrar_home(request):
    render(request, 'index.html')

def criar_email(request): 
    pass

