from django.shortcuts import render
from tienda.models import Producto   

def home(request):
    # Trae los productos destacados (máximo 6)
    productos = Producto.objects.filter(destacado=True)[:6]
    return render(request, 'core/home.html', {'productos': productos})

def garantias(request):
    return render(request, 'core/garantias.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')
