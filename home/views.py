import http
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from login.views import login,cadastro
from login.views import valida_cadastro, valida_login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from home.models import Cdntv, VOD, Aplicativos, Origindown, Downedge, Downvod, Downoriginvod, Downedgevod
import re
from django.conf import settings



def home(request):
    if request.session['logado']:
        return render(request, 'home.html')
    
    else:
        return redirect('/auth/login/?status=2')
    
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
        envia_email = EmailMultiAlternatives(f'CDNTV[#{demanda}] - {provedor} - Implementação do serviço', text_content, settings.EMAIL_HOST_USER, [email], None, None, None, None, None,['@ativacoes.technobox'])
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
        self_email = request.POST.get('self_email')
        demanda3 = request.POST.get('demanda3')
        nprovedor2 = request.POST.get('nprovedor2')
        
        
        aplicativos = Aplicativos(
            nome = nome,
            mobile = mobile,
            stb = stb,
            ios = ios, 
            apks = apks,
            self_email = self_email,
            email3 = email3,
            demanda3 = demanda3, 
            nprovedor2 = nprovedor2
        )        
        aplicativos.save()
        
        html_content = render_to_string('email/emailapp.html',{'nome': nome, 'mobile': mobile, 'stb':stb, 'ios': ios, 'apks' : apks, 'email3' : email3, 'demanda3' : demanda3, 'nprovedor2' : nprovedor2})
        text_content = strip_tags(html_content)
        envia_email = EmailMultiAlternatives(f'CDNTV[#{demanda3}] - {nprovedor2} - Criação dos aplicativos', text_content, self_email, [email3], None, None, None, None, None, ['ziksduarte@gmail.com'])
        envia_email.attach_alternative(html_content, 'text/html')
        envia_email.send()
        return render(request, 'confirma.html')

def down(request):
    if request.method == 'GET':
        return render(request, 'down.html')
    
def downorigin(request):
    if request.method == 'GET':
        return render(request, 'down_origin.html')
    
    elif request.method == 'POST':
        origin4 = request.POST.get('origin4')
        email4 = request.POST.get('email4')
        ndemanda4 = request.POST.get('ndemanda4')
        nprovdor4 = request.POST.get('nprovedor4')
        
        down_origin = Origindown(
            origin4 = origin4,
            email4= email4,
            ndemanda4 = ndemanda4,
            nprovdor4 = nprovdor4
        )
        
        down_origin.save()
 
    #html_content = render_to_string('email/emailapp.html',{'nome': nome, 'mobile': mobile, 'stb':stb, 'ios': ios, 'apks' : apks, 'email3' : email3, 'demanda3' : demanda3, 'nprovedor2' : nprovedor2})
    #text_content = strip_tags(html_content)
    #envia_email = EmailMultiAlternatives(f'CDNTV[#{demanda3}] - {nprovedor2} - Criação dos aplicativos', text_content, self_email, [email3], None, None, None, None, None, ['ziksduarte@gmail.com'])
    #envia_email.attach_alternative(html_content, 'text/html')
    #envia_email.send()
    #return render(request, 'confirma.html')
    ##


def downedge(request):
    if request.method == 'GET':
        return render(request, 'down_edge.html' )
    
    elif request.method == 'POST':
        edge5 = request.POST.get('edge5')
        email5 = request.POST.get('email5')
        ndemanda5 =  request.POST.get('ndemanda5')
        nprovedor5 =  request.POST.get('nprovedor5')
        
        downedge = Downedge( 
        edge5 = edge5,
        email5 = email5,
        ndemanda5 = ndemanda5, 
        nprovedor5 = nprovedor5
        )
        
        downedge.save()
        
   
   #html_content = render_to_string('email/emailapp.html',{'nome': nome, 'mobile': mobile, 'stb':stb, 'ios': ios, 'apks' : apks, 'email3' : email3, 'demanda3' : demanda3, 'nprovedor2' : nprovedor2})
    #text_content = strip_tags(html_content)
    #envia_email = EmailMultiAlternatives(f'CDNTV[#{demanda3}] - {nprovedor2} - Criação dos aplicativos', text_content, self_email, [email3], None, None, None, None, None, ['ziksduarte@gmail.com'])
    #envia_email.attach_alternative(html_content, 'text/html')
    #envia_email.send()
    #return render(request, 'confirma.html')

    return render(request, 'confirma.html')


def downvod(request):
    if request.method == 'GET':
        return render(request, 'down_vod.html')
    
    elif request.method == 'POST':
        vod = request.POST.get('vod')
        email6 = request.POST.get('email6')
        ndemanda6 = request.POST.get('ndemanda6')
        nprovedor6 = request.POST.get('nprovedor6')
        
        downvod = Downvod(
            vod = vod, 
            email6 = email6,
            ndemanda6 = ndemanda6,
            nprovedor6 = nprovedor6
        )
        
        downvod.save()
    
        return render(request, 'confirma.html')
    
    
def downoriginvod(request):
    if request.method == 'GET':
        return render(request, 'down_originvod.html')
    
    elif request.method == 'POST':
        origin7 = request.POST.get('origin6')
        vod1 = request.POST.get('vod')
        email7 = request.POST.get('email7')
        ndemanda7 = request.POST.get('ndemanda7')
        nprovedor7 = request.POST.get('nprovedor7')
        
        downoriginvod = Downoriginvod(
            origin7 = origin7,
            vod1 = vod1,
            email7 = email7,
            ndemanda7 = ndemanda7,
            nprovedor7 = nprovedor7
        ) 
        
        downoriginvod.save()
        
    #html_content = render_to_string('email/emailapp.html',{'nome': nome, 'mobile': mobile, 'stb':stb, 'ios': ios, 'apks' : apks, 'email3' : email3, 'demanda3' : demanda3, 'nprovedor2' : nprovedor2})
    #text_content = strip_tags(html_content)
    #envia_email = EmailMultiAlternatives(f'CDNTV[#{demanda3}] - {nprovedor2} - Criação dos aplicativos', text_content, self_email, [email3], None, None, None, None, None, ['ziksduarte@gmail.com'])
    #envia_email.attach_alternative(html_content, 'text/html')
    #envia_email.send()

    return render(request, 'confirma.html')


def downedgevod(request):
    if request.method == 'GET':
        return render(request, 'down_edgevod.html')        
    
    elif request.method == 'POST':
        edge8 = request.POST.get('edge8')
        vod2 = request.POST.get('vod2')
        email8 = request.POST.get('email8')
        ndemanda8 = request.POST.get('ndemanda8')
        nprovedor8 = request.POST.get('nprovedor8')
        
        downedgevod = Downedgevod(
            edge8 = edge8,
            vod2 = vod2,
            email8 = email8,
            ndemanda8 = ndemanda8,
            nprovedor8 = nprovedor8
        )
        
        downedgevod.save()
        
    #html_content = render_to_string('email/emailapp.html',{'nome': nome, 'mobile': mobile, 'stb':stb, 'ios': ios, 'apks' : apks, 'email3' : email3, 'demanda3' : demanda3, 'nprovedor2' : nprovedor2})
    #text_content = strip_tags(html_content)
    #envia_email = EmailMultiAlternatives(f'CDNTV[#{demanda3}] - {nprovedor2} - Criação dos aplicativos', text_content, self_email, [email3], None, None, None, None, None, ['ziksduarte@gmail.com'])
    #envia_email.attach_alternative(html_content, 'text/html')
    #envia_email.send()

    return render(request, 'confirma.html')

    
        
        
        
  
