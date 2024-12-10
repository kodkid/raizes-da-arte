from django.shortcuts import render

TEMPLATES = [
    {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': 'raizes_da_arte/template',
    }
]

# Create your views here.
def raizes_da_arte(request):
    return render(request, 'index.html')