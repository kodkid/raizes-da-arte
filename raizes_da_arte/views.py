from django.shortcuts import render

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
    return render(request, 'cadastro.html')

def perfil(request):
    return render(request, 'perfil.html')

def meu_perfil(request):
    return render(request, 'meu-perfil.html')

