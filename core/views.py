from django.shortcuts import render
from core.models import Producto

def home(request):
    productos = Producto.objects.filter(destacado=True)[:6]  # o todos si querés
    return render(request, 'core/home.html', {'productos': productos})

def garantias(request):
    return render(request, 'core/garantias.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')


