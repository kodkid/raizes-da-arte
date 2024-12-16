from django.db import models

# Mudança nas models: em related_name nomes repetidos não são repetidos , foi criado nomes diferentes
class User(models.Model):
    postagens = models.ManyToManyField('Postagem', related_name='usuario_postagem')
    nome = models.CharField(max_length=50 , null=True )
    email = models.EmailField(max_length=50 , unique=True ) #Email nao pode ser repetido
    senha = models.CharField(max_length=500 )
    cep = models.CharField(max_length=50) #Adicionado CEP 
    descricao = models.TextField()
    categoria = models.CharField(max_length=50)
    imagem_perfil = models.FilePathField(path="/img") 


class Postagem(models.Model):
    usuario = models.ForeignKey('User', on_delete=models.CASCADE, related_name='postagem_usuario')
    curtidas = models.IntegerField(default=0) #CONTADOR DOS LIKES HAHAHAHA
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagens = models.ManyToManyField('Imagem', related_name='postagens_imagem')  # (Muitos IMAGENS para uma POSTAGEM)
    comentarios = models.ManyToManyField('Comentario', related_name='postagens_comentario')  # (Muitos COMENTÁRIOS para uma POSTAGEM)


   
class Comentario(models.Model):
    postagem = models.ForeignKey('Postagem', on_delete=models.CASCADE, related_name='comentario_postagem')
    texto = models.TextField()  
    # Comentário da POSTAGEM ;) 


class Imagem(models.Model):
    postagem = models.ForeignKey('Postagem', on_delete=models.CASCADE, related_name='imagens_postagem')
    urlImagem = models.TextField()  
    # Imagem da POSTAGEM :)


