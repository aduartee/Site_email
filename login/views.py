from django.shortcuts import render,redirect
from django.http import HttpResponse
from login.models import Login, Cadastrar
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from hashlib import sha256
from django.contrib.auth import login as login_django

def home(request):
    return render(request,'home.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def valida_cadastro(request):
    usuario2 = request.POST.get('usuario2')
    email2 = request.POST.get('email2')
    senha2 = request.POST.get('senha2')
    confirmasenha = request.POST.get('confirmasenha')
    
    ## Valida se o usuario não digitou nada no campo de usuario
    if len(usuario2.strip()) == 0 or len(usuario2.strip()) == 0:
        # Vai redirecionar para a pagina de login, será passado um status = 1 
        return redirect('/auth/cadastro/?status=1')
    
    # Valida se a senha é menor que 4 digitos, se for, vai ser passado um status = 2
    if len(senha2) < 4:
        return redirect('/auth/cadastro/?status=2')
    
    # Verifica se já existe algum outro usuario com esse email
    cadastro = Cadastrar.objects.filter(email2 = email2)
    
    # Nesse caso, se o tamanho for maior que 0, logo ele existe, então ele retorna um status = 3
    if len(cadastro) > 0:
        return redirect('/auth/cadastro/?status=3')
    
    try:
        # responsavel por criptografar a senha que vai ser salva
        senha2 = sha256(senha2.encode()).hexdigest()
        
        cadastro = Cadastrar(
            usuario2 = usuario2,
            email2 = email2,
            senha2 = senha2,
            confirmasenha = confirmasenha
        )
        cadastro.save()
        return redirect('/auth/cadastro/?status=0')

    except:
        return redirect('/auth/cadastro/?status=4')
    
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        
        if campos_vazios(usuario, senha):
            return redirect('login')
        
        
        user = authenticate(usuario=usuario, password=senha)
        
        login = Login(
            usuario = usuario,
            senha = senha
        )
        
        login.save()
        if user: 
            login_django(request, user)
            return redirect('home')
    
    
    return HttpResponse('Login realizado')


def logout(request):
    pass

def senhas_nao_iguais(senha,senha2):
    return senha != senha2
    
def usuario_existente():
    pass
        
        
def campos_vazios(email,senha):
    return email == "" or senha == ""

    