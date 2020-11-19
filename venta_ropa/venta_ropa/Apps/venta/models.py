from django.db import models

# Create your models here.

class Facturacion(models.Model):
    Apellido = models.CharField(max_length=30)
    Nombres = models.CharField(max_length=30)
    Direccion = models.CharField(max_length=30)
    Nit = models.CharField(max_length=10)

    def NombreCompleto(self):
        cadena = "{0}, {1}"
        return cadena.format(self.Apellido, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()

class Ropa(models.Model):
    Ropas = (('C', 'Camisa'), ('P', 'Pantalon'), ('S', 'Sueter'))
    Ropass = models.CharField(max_length=1, choices=Ropas, default='C')
    cantidad = models.PositiveIntegerField(default=True)
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return "{0}, ({1})".format(self.Ropass, self.cantidad)

class Tarjeta(models.Model):
    Nombre = models.CharField(max_length=20)
    Numero = models.CharField(max_length=15)
    Fecha = models.DateField()
    CVV = models.CharField(max_length=4)

    def NTarjeta(self):
        cadena2 = "{0}, {1}"
        return cadena2.format(self.Nombre, self.Numero)


    def __str__(self):
        return self.NTarjeta()

class Pedido(models.Model):
    Facturacion = models.ForeignKey(Facturacion, null=False, blank=False, on_delete=models.CASCADE)
    Ropa = models.ForeignKey(Ropa, null=False, blank=False, on_delete=models.CASCADE)
    Tarjeta = models.ForeignKey(Tarjeta, null=False, blank=False, on_delete=models.CASCADE)
    Pedido = models.DateTimeField(auto_now=True)

    def __str__(self):
        cadena3 = "{0} => {1}"
        return cadena3.format(self.Facturacion, self.Ropa.Ropass) 
