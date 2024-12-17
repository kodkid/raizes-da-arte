from django.shortcuts import render, redirect  # Importando check_password
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import User  # Certifique-se de que User está corretamente configurado no seu projeto


# Exemplo de view da página inicial
def raizes_da_arte(request):
    return render(request, 'index.html')

# Função de login
def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')  # Se o usuário já estiver autenticado, redireciona para a página inicial
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not email:
            messages.error(request, "O campo de email não pode estar vazio.")
            return redirect('login')      
        print(f"Tentando login com email: {email} e password: {password}")
        # Usar authenticate com 'username=email' pois USERNAME_FIELD é 'email'
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('index')  # Redireciona para a página inicial após login

        else:
            # Verifica se o usuário existe para informar o erro específico
            if not User.objects.filter(email=email).exists():
                messages.error(request, "Email não encontrado.")
            else:
                messages.error(request, "Senha incorreta.")
            return redirect('login')  # Redireciona para a página de login se falhar
    else:
        return render(request, 'login.html')

# Função de cadastro
def cadastro(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        cep = request.POST.get('cep')


        
          # Codificando a password em hash

        # Verificando se o email já está cadastrado
        if User.objects.filter(email=email).exists():
            messages.error(request, "Este email já está cadastrado.")
  
            return redirect('cadastro')  # Redireciona para a página de cadastro
        if (len(password) < 8):
            messages.error(request, "A password deve conter pelo menos 8 caracteres.")
            return redirect('cadastro')
        # Criando o usuário
        user = User.objects.create(
            email=email,
            cep=cep
        )
        user.set_password(password)
        user.save()
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

def inicio(request):
    return render(request, 'inicio.html')

@login_required
def login_view(request):
    return render(request, 'index.html')

    
