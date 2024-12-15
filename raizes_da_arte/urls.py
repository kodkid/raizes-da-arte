# urls.py
from django.urls import path
from raizes_da_arte import views

urlpatterns = [
    path('', views.raizes_da_arte, name='index.html'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perfil/', views.perfil, name='perfil'),
    path('meu-perfil/', views.meu_perfil, name='meu-perfil'),
    path('perfis/', views.perfis, name='perfis'),
    path('eventos/', views.eventos, name='eventos'),
]
