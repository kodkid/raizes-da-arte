# urls.py
from django.urls import path
from raizes_da_arte import views

urlpatterns = [
    path('', views.raizes_da_arte, name='index.html'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perfil/', views.perfil, name='perfil'),
]
