from django.db import models


class User(models.Model):
    postagens = models.ManyToManyField('Postagem', related_name='usuarios')
    nome = models.CharField(max_length=50 )
    email = models.EmailField(max_length=50 )
    senha = models.CharField(max_length=500 )
    descricao = models.TextField()
    categoria = models.CharField(max_length=50)
    imagem_perfil = models.FilePathField(path="/img") 


class Postagem(models.Model):
    usuario = models.ForeignKey('User', on_delete=models.CASCADE, related_name='postagens')
    curtidas = models.IntegerField(default=0) #CONTADOR DOS LIKES HAHAHAHA
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagens = models.ManyToManyField('Imagem', related_name='postagens')  # (Muitos IMAGENS para uma POSTAGEM)
    comentarios = models.ManyToManyField('Comentario', related_name='postagens')  # (Muitos COMENTÁRIOS para uma POSTAGEM)


   
class Comentario(models.Model):
    postagem = models.ForeignKey('Postagem', on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()  
    # Comentário da POSTAGEM ;) 


class Imagem(models.Model):
    postagem = models.ForeignKey('Postagem', on_delete=models.CASCADE, related_name='imagens')
    urlImagem = models.TextField()  
    # Imagem da POSTAGEM :)


