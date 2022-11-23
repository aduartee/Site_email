from django.shortcuts import render,redirect
from django.http import HttpResponse
from login.models import Cadastrar
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from hashlib import sha256
from django.template.loader import render_to_string
from django.contrib.auth import login as login_django
from django.utils.html import strip_tags



def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def valida_cadastro(request):
    usuario2 = request.POST.get('usuario2')
    senha2 = request.POST.get('senha2')
    confirmasenha = request.POST.get('confirmasenha')
    
    ## Valida se o usuario não digitou nada no campo de usuario
    if len(usuario2.strip()) == 0 or len(senha2.strip()) == 0:
        # Vai redirecionar para a pagina de login, será passado um status = 1 
        return redirect('/auth/cadastro/?status=1')
    
    # Valida se a senha é menor que 4 digitos, se for, vai ser passado um status = 2
    if len(senha2) < 4:
        return redirect('/auth/cadastro/?status=2')
    
    if senhas_diferentes(senha2, confirmasenha):
        return redirect('/auth/cadastro/?status=10')
    
    
    # Verifica se já existe algum outro usuario com esse email
    cadastro = Cadastrar.objects.filter(usuario2 = usuario2)
    
    # Nesse caso, se o tamanho for maior que 0, logo ele existe, então ele retorna um status = 3
    if len(cadastro) > 0:
        return redirect('/auth/cadastro/?status=3')
    
    try:
        # responsavel por criptografar a senha que vai ser salva
        senha2 = sha256(senha2.encode()).hexdigest()
        
        cadastro = Cadastrar(
            usuario2 = usuario2,
            senha2 = senha2,
            confirmasenha = confirmasenha
        )
        cadastro.save()
        return redirect('/auth/cadastro/?status=0')

    except:
        return redirect('/auth/cadastro/?status=4')
        
def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})
    
def valida_login(request):
    usuario2 = request.POST.get('usuario2')
    senha2= request.POST.get('senha2')
    
    senha2 = sha256(senha2.encode()).hexdigest()
    
    # Faz a validação se o usuario e senha existe no banco de dados
    usuario = Cadastrar.objects.filter(usuario2 = usuario2).filter(senha2 = senha2)
    
    # Se o usuario não existe, ele retorna um status = 0
    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    
    
    # Se o usuario existe, ele envia para o a pagina home. Nessa situação usei o session para realizar o login
    elif len(usuario) > 0:
        request.session['logado'] = True
        return redirect('/home')
        
def logout(request):
    request.session['logado'] = None
    return redirect('/auth/login')
    
def senhas_diferentes(senha,senha2):
    return senha != senha2
    
     
def campos_vazios(email,senha):
    return email == "" or senha == ""

    