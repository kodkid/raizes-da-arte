from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password, check_password 

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O email deve ser fornecido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Usa o método set_password para fazer o hash da password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# Mudança nas models: em related_name nomes repetidos não são repetidos , foi criado nomes diferentes
class User(AbstractBaseUser):
    postagens = models.ManyToManyField('Postagem', related_name='usuario_postagem')
    name = models.CharField(max_length=50 , null=True )
    email = models.EmailField(max_length=50 , unique=True ) #Email nao pode ser repetido
    password = models.CharField(max_length=500 )
    cep = models.CharField(max_length=50) #Adicionado CEP 
    descricao = models.TextField()
    categoria = models.CharField(max_length=50)
    imagem_perfil = models.FilePathField(path="/img", null=True , blank=True) 

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Definir o campo 'USERNAME_FIELD' como 'email' (campo para autenticação)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']  # Campos obrigatórios para criar um superusuário

    # Usar o UserManager para manipulação do usuário
    objects = UserManager()

    def __str__(self):
        return self.email
    def set_password(self, raw_password):
        """Método para hash da senha."""
        self.password = make_password(raw_password)
        self._password = raw_password  # Armazenar a senha original para a validação

    def check_password(self, raw_password):
        """Método para verificar se a senha corresponde ao hash."""
        return check_password(raw_password, self.password)
    


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


