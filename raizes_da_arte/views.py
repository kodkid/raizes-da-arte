from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password 
from django.contrib import messages  # Importando o sistema de mensagens
from django.contrib.auth import authenticate, login
from .models import User
TEMPLATES = [
    {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': 'raizes_da_arte/templates',
    }
]

# Create your views here.
def raizes_da_arte(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    # Captando os dados do usuario da pagina cadastro
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('password')
        cep = request.POST.get('cep')
        
        senha_hash = make_password(senha) # 'Codigo para converter senha em hash'
        #Transformando os dados do usuario em um objeto chamado user

        # Verificando se o email já existe no banco
        if User.objects.filter(email=email).exists():
            messages.error(request, "Este email já está cadastrado.")
            return redirect('cadastro')  # Redireciona para a página de cadastro
        
        user = User.objects.create(  
            email=email,
            senha=senha_hash,
            cep=cep
        )

        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('login')

        
    return render(request, 'cadastro.html')

def perfil(request):
    return render(request, 'perfil.html')

def meu_perfil(request):
    return render(request, 'meu-perfil.html')

def perfis(request):
    return render(request, 'perfis.html')

def eventos(request):
    return render(request, 'eventos.html')



    
