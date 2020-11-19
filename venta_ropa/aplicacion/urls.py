from django.urls import path
from .views import homepage, contacto, imagenes, registro 
# agregar_producto, listar_productos

urlpatterns = [
    path('', homepage, name="homepage"),
    path('contacto/', contacto, name="contacto"),
    path('imagenes/', imagenes, name="imagenes"),
    path('registro/', registro, name="registro"),
] 

'''
    path('agregar-productos/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_producto"),    '''