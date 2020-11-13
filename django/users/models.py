"""
    Modelo Proxy para usuarios de nuestro sistema
"""

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=8, blank=True)
    userImage = models.ImageField(
        upload_to = "users/pictures",
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
'''
#from django.db import models


class Usuario(models.Model):
    nombrecompleto = models.TextField(db_column='Nombrecompleto', blank=True, null=True)  # Field name made lowercase.
    nombredeusuario = models.TextField(db_column='NombredeUsuario', blank=True, null=True)  # Field name made lowercase.
    correoelectronico = models.TextField(db_column='CorreoElectronico', blank=True, null=True)  # Field name made lowercase.
    edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
    fotografia = models.TextField(db_column='Fotografia', blank=True, null=True)  # Field name made lowercase.
    contraseña = models.TextField(db_column='Contraseña', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
        '''

      

