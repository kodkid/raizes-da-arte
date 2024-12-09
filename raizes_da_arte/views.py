from django.shortcuts import render

# Create your views here.
def raizes_da_arte(request):
    return render(request, 'index.html')