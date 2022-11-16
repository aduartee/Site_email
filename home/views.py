import http
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from login.views import login,cadastro
from login import models
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from home.models import Cdntv, VOD, Aplicativos
import re
from django.conf import settings


def cdntv(request):
    ### Se a request for do tip GET, o retorno será a pagina renderizada novamente
    if request.method == "GET":
        return render(request, 'cdntv.html')
    
    ### Caso request for um metodo POST, guarda os valores do form em uma variavel
    elif request.method == "POST":
        origin = request.POST.get('origin')
        senha = request.POST.get('senha')
        edge = request.POST.get('edge')
        email = request.POST.get('email')
        demanda = request.POST.get('demanda')
        provedor = request.POST.get('provedor')
        
        cdntv = Cdntv(
           origin = origin,
           senha = senha,
           edge = edge,
           email = email,
           demanda = demanda,
           provedor = provedor
        )
        
        cdntv.save()
        html_content = render_to_string('email\emailcdntv.html',{'origin': origin, 'senha': senha, 'edge':edge, 'email': email})
        text_content = strip_tags(html_content)
        envia_email = EmailMultiAlternatives(f'CDNTV[#{demanda}] - {provedor} - Implementação do serviço', text_content, settings.EMAIL_HOST_USER, [email])
        envia_email.attach_alternative(html_content, 'text/html')
        envia_email.send()
        
        return render(request, 'confirma.html')
     
    # Validando se o usuario está digitando um email valido
    if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
        return render(request, 'cdntv.html', {'orgin': origin, 'senha': senha, 'edge':edge, 'demanda': demanda, 'provedor':provedor})
    
    
    return HttpResponse('Email CDNTV enviado!')


def vod(request):
    if request.method == "GET":
        return render(request, 'vod.html')
    
    elif request.method == "POST":
        origin2 = request.POST.get('origin2')
        edge2 = request.POST.get('edge2')
        email2 = request.POST.get('email2')
        demanda2 = request.POST.get('demanda2')
        nprovedor = request.POST.get('nprovedor')
        
        
        vod = VOD(
            origin2 = origin2,
            edge2 = edge2,
            email2 = email2,
            demanda2 = demanda2,
            nprovedor = nprovedor
        )
        vod.save()
        
        html_content = render_to_string('email\emailvod.html',{'origin2': origin2, 'edge2': edge2, 'email2':email2, 'demanda2': demanda2, 'nprovedor' : nprovedor})
        text_content = strip_tags(html_content)
        envia_email = EmailMultiAlternatives(f'CDNTV[#{demanda2}] - {nprovedor} - Implementação VOD', text_content, settings.EMAIL_HOST_USER, [email2])
        envia_email.attach_alternative(html_content, 'text/html')
        envia_email.send()
        return render(request, 'confirma.html')
        
        
    if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email2):
        return render(request, 'cdntv.html', {'orgin2': origin2, 'edge2':edge2, 'email2': email2 ,'demanda2': demanda2, 'provedor2': nprovedor})
        
    return HttpResponse('Email do VOD enviado')
        
        
def aplicativos(request):
    if request.method == 'GET':
        return render(request, 'aplicativos.html')
    
    elif request.method == 'POST':
        nome = request.POST.get('nome') 
        mobile = request.POST.get('mobile')
        stb = request.POST.get('stb')
        ios = request.POST.get('ios')
        apks = request.POST.get('apks')
        email3 = request.POST.get('email3')
        demanda3 = request.POST.get('demanda3')
        nprovedor2 = request.POST.get('nprovedor2')
        
        
        aplicativos = Aplicativos(
            nome = nome,
            mobile = mobile,
            stb = stb,
            ios = ios, 
            apks = apks,
            email3 = email3,
            demanda3 = demanda3, 
            nprovedor2 = nprovedor2
            
        )        
        aplicativos.save()
        
        html_content = render_to_string('email\emailvod.html',{'nome': nome, 'mobile': mobile, 'stb':stb, 'ios': ios, 'apks' : apks, 'email3' : email3, 'demanda3' : demanda3, 'nprovedor2' : nprovedor2})
        text_content = strip_tags(html_content)
        envia_email = EmailMultiAlternatives(f'CDNTV[#{demanda3}] - {nprovedor2} - Criação dos aplicativos', text_content, settings.EMAIL_HOST_USER, [email3])
        envia_email.attach_alternative(html_content, 'text/html')
        envia_email.send()
        return render(request, 'confirma.html')
    

def envia_email(request):
    return render(request, 'cdntv.html')

def home(request):
    if request.session['logado']:
        return render(request, 'home.html')
    
    else:
        return redirect('/auth/login/?status=2')
    

    

