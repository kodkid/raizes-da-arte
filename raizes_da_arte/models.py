from django.db import models

# Create your models here.

class user(models.Model):
    idPostagem = models.IntegerField(),
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=500)
    descricao = models.TextField()
    categoria = models.CharField(max_length=50)


