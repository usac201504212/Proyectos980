from django.shortcuts import render, redirect
from .models import Producto 
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.
 
def homepage(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'aplicacion/homepage.html', data)

def contacto(request):
    return render(request, 'aplicacion/contacto.html')

def imagenes(request):
    return render(request, 'aplicacion/imagenes.html')


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="homepage")
        data["form"] = formulario
        
    

    return render(request, 'registration/registro.html', data)




'''
from django.shortcuts import render
from.models import Producto
from .forms import ContactoForm, ProductoForm

# Create your views here.
def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)

def contacto(request):
    data = {
        'form': ContactoForm()      #Creando una instancia
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Conctacto guardado"
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

def galeria(request):
    return render(request, 'app/galeria.html')

def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'app/producto/agregar.html', data)

def listar_productos(request):
    product = Producto.objects.all()

    data = {
        'product': product
    }
'''