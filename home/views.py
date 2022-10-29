import http
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from . models import Cdntv
import re
from django.conf import settings


def perfil(request): 
    pass

def vod(request):
    return render(request, 'vod.html')

def cdntv(request):
    ### Se a request for do tip GET, o retorna será a pagina renderizada novamente
    if request.method == "GET":
        return render(request, 'cdntv.html')
    
    ### Caso retorno for um metodo POST, guarda os valores do form em uma variavel
    elif request.method == "POST":
        origin = request.POST.get('origin')
        senha = request.POST.get('senha')
        edge = request.POST.get('edge')
        email = request.POST.get('email')
        titulo = request.POST.get('titulo')
        
        cdntv = Cdntv(
           origin = origin,
           senha = senha,
           edge = edge,
           email = email,
           titulo = titulo
        )
        
        cdntv.save()
        html_content = render_to_string('email\emailcdntv.html',{'origin': origin, 'senha': senha, 'edge':edge, 'email': email, 'titulo':titulo})
        text_content = strip_tags(html_content)
        
        email = EmailMultiAlternatives({'titulo': titulo}, text_content)
        return render(request, 'confirma.html')
    
   
    
    
     
        
    if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
        return render(request, 'cdntv.html', {'orgin': origin, 'senha': senha, 'edge':edge, 'titulo':titulo})
    
    
    return HttpResponse('Email enviado!')

        
        

def aplicativos(request):
    return render(request, 'aplicativos.html')

def envia_email(request):
    return render(request, 'cdntv.html')

def home(request):
    return render(request, 'home.html')
