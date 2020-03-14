from django.db import models

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    """
        Extendemos de la clase de Usuarios y le agregamos mas datos 
        tomando de base ese modelo
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length = 200, blank = True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank = True)

    """
        Usango el ImageField se guarda la referencia hacia el archivo, 
        en la carpeta donde se indica.
        Para usar ImageField se debe de instalar Pillow
    """ 
    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


def __string__(self):
    return self.user.username