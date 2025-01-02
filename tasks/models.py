from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, username, email, nombres, apellidos, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        usuario = self.model(
            username = username,
            email = self.normalize_email(email),
            nombres = nombres,
            apellidos = apellidos
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self, username, email, nombres, apellidos, password=None):
        usuario = self.create_user(
            username = username,
            email = email,
            nombres = nombres,
            apellidos = apellidos,
            password = password
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

class Usuario(AbstractUser):
    username = models.CharField('Nombre de usuario', max_length=255, unique=True)
    email = models.EmailField('Correo Electrónico', max_length=255, unique=True)
    nombres = models.CharField('Nombres', max_length=255, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=255, blank=True, null=True)
    imagen = models.ImageField('Imagen de Perfil', upload_to='perfil/', max_length=255, null=True, blank=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    rol = models.CharField('Rol', max_length=255, blank=True, null=True)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
    
    def has_perms(self, perm_list, obj = None):
        return True
    
    def has_perm(self, perm, obj = None):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador
    
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title