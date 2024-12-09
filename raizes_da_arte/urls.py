# urls.py
from django.urls import path
from raizes_da_arte import views

urlpatterns = [
    path('', views.raizes_da_arte, name='raizes_da_arte'),
]
