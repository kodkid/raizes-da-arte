from django.shortcuts import render , redirect
# from django.contrib.auth.hashers import make_password 'importando codigo para converter senha em hash'
from django.http import HttpResponse
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
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
       # senha_hash = make_password(senha) 'Codigo para converter senha em hash'
        #Transformando os dados do usuario em um objeto chamado user
        user = User.objects.create(  
            nome=nome,
            email=email,
            senha=senha
        )

        
        return redirect('sucesso')
        return HttpResponse(f"Cadastro realizado com sucesso! Email: {email}, CEP: {cep}")
    return render(request, 'cadastro.html')

def perfil(request):
    return render(request, 'perfil.html')

def meu_perfil(request):
    return render(request, 'meu-perfil.html')

def perfis(request):
    return render(request, 'perfis.html')

def eventos(request):
    return render(request, 'eventos.html')



    
