from django.db import models

class Postagem(models.Model):
    titulo = models.Charfield(max_length=255)
    corpo = models.TextField()
    criado_em = models.Datatimefield(auto_now_add=True)
    ultima_modificacao = models.DateTimeField(auto_now=True)
    categorias = models.ManyToManyField('Categoria', related_name='postagem')


class Comentario(models.Model):
    autor = models.CharField(max_lenght=60)
    corpo = models.TextField()
    criado_em = models.DateTimeField(auuto_now_add=True)
    postagem = models.ForeignKey('Postagem', on_delete=models.CASCADE)