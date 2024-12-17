from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password  # Importando check_password
from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login
from .models import User  # Certifique-se de que User está corretamente configurado no seu projeto


# Exemplo de view da página inicial
def raizes_da_arte(request):
    return render(request, 'index.html')

# Função de login
def login(request):
    if request.user.is_authenticated:
        return redirect('index')  # Se o usuário já estiver autenticado, redireciona para a página inicial
    
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('password')
        
        # Usar authenticate com 'username=email' pois USERNAME_FIELD é 'email'
        user = authenticate(request, email=email, password=senha)

        if user is not None:
            django_login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('index')  # Redireciona para a página inicial após login
        else:
            messages.error(request, "Credenciais inválidas.")
            return redirect('login')  # Redireciona para a página de login se falhar
    else:
        return render(request, 'login.html')

# Função de cadastro
def cadastro(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('password')
        cep = request.POST.get('cep')


        
        senha_hash = make_password(senha)  # Codificando a senha em hash

        # Verificando se o email já está cadastrado
        if User.objects.filter(email=email).exists():
            messages.error(request, "Este email já está cadastrado.")
  
            return redirect('cadastro')  # Redireciona para a página de cadastro
        if (len(senha) < 8):
            messages.error(request, "A senha deve conter pelo menos 8 caracteres.")
            return redirect('cadastro')
        # Criando o usuário
        user = User.objects.create(
            email=email,
            senha=senha_hash,  # Certifique-se de que o campo de senha está correto no seu modelo
            cep=cep
        )
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('login')  # Redireciona para a página de login após o cadastro
    return render(request, 'cadastro.html')

# Outras views
def perfil(request):
    return render(request, 'perfil.html')

def meu_perfil(request):
    return render(request, 'meu-perfil.html')

def perfis(request):
    return render(request, 'perfis.html')

def eventos(request):
    return render(request, 'eventos.html')
