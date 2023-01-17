from django.shortcuts import render,redirect
from django.http import HttpResponse
from login.models import Cadastrar
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from hashlib import sha256
from django.template.loader import render_to_string
from django.contrib.auth import login as login_django
from django.utils.html import strip_tags
from django.contrib import messages, auth
from django.contrib.messages import constants
from django.contrib.auth.models import User


def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def valida_cadastro(request):
    usuario2 = request.POST.get('usuario2')
    email = request.POST.get('email')
    senha2 = request.POST.get('senha2')
    confirmasenha = request.POST.get('confirmasenha')
    
    ## Valida se o usuario não digitou nada no campo de usuario
    if len(usuario2.strip()) == 0 or len(senha2.strip()) == 0:
        # Vai redirecionar para a pagina de login, será passado um status = 1 
        messages.add_message(request, constants.ERROR,'Os campos não podem ficar vazios')
        return redirect('/auth/cadastro/')
    
    if len(email.strip()) == 0:
        messages.add_message(request, constants.ERROR,'O campo email deve ser preenchido')
        return redirect('/auth/cadastro/')
     
    # Valida se a senha é menor que 4 digitos, se for, vai ser passado um status = 2
    if len(senha2) < 4:
        messages.add_message(request, constants.ERROR,'Sua senha deve possuir no minimo quatro caracteres')
        return redirect('auth/cadastro/')
    
    if senhas_diferentes(senha2, confirmasenha):
        messages.add_message(request, constants.ERROR,'As senhas devem ser iguais')
        return redirect('/auth/cadastro/')
    
    
    # Verifica se já existe algum outro usuario com esse email
    if User.objects.filter(email = email).exists():
        messages.add_message(request, constants.ERROR,'Email já foi cadastrado')
        return redirect('/auth/cadastro/')
    
    if User.objects.filter(username = usuario2).exists():
        messages.add_message(request, constants.ERROR,'Usuário já foi cadastrado')
        return redirect('/auth/cadastro/')
    
    try:
        cadastro = User.objects.create_user(username = usuario2, email= email, password= senha2)
        cadastro.save()
        
        #Mensagem de sucesso
        messages.add_message(request, constants.SUCCESS,'Usuário cadastrado com sucesso')
        return redirect('/auth/cadastro/')

    except:
        messages.add_message(request, constants.ERROR,'Erro interno')
        return redirect('/auth/cadastro/')
        
def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})
    
def valida_login(request):
    usuario2 = request.POST.get('usuario2')
    email = request.POST.get('email')
    senha2= request.POST.get('senha2')
    
    
    # Faz a validação se o usuario, senha e email existem no banco de dados
    usuario = auth.authenticate(request, username= usuario2, email=email, password=senha2)
    
    # Se o usuario não existe, ele retorna um status = 0
    if not usuario:
        messages.add_message(request, constants.ERROR,'Email ou senha invalidos')
        return redirect('/auth/login/')
    
    #Autentica o usuario caso ele exista
    else:
        auth.login(request, usuario)
        return redirect('/home/')
        
def logout(request):
    auth.logout(request)
    return redirect('/auth/login')
    
def senhas_diferentes(senha,senha2):
    return senha != senha2
    
     
def campos_vazios(email,senha):
    return email == "" or senha == ""

    