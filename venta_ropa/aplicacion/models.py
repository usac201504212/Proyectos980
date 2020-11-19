from django.db import models

# Create your models here.
class UserProfile(models.Model):
    Nombrecompleto = models.CharField(max_length=35)  # Field name made lowercase.
    Nombreusuario = models.CharField(max_length=35)  # Field name made lowercase.
    Correo = models.CharField(max_length=35)  # Field name made lowercase.
    Edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
    Fotografia = models.ImageField( upload_to = "pictures", null=True) 
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)   
    
     

class Producto(models.Model):
    Nombre = models.CharField(max_length=35)  # Field name made lowercase.
    Precio = models.IntegerField(db_column='Precio', blank=True, null=True)  
    Imagen = models.ImageField( upload_to = "productos", null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
     

class Contacto(models.Model):
    usuario = models.CharField(max_length=20)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    correo = models.EmailField()
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre 



     
