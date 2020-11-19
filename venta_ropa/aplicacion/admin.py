from django.contrib import admin
from .models import Producto, Contacto, UserProfile
# Register your models here.

admin.site.register(Producto)
admin.site.register(Contacto)
admin.site.register(UserProfile) 