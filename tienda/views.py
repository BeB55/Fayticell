from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from core.models import Producto

def inicio(request):
    return HttpResponse("Bienvenido a Fayticell - Tu servicio tecnico de confianza.")


def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    # Buscar productos relacionados por categoría
    relacionados = Producto.objects.filter(
        categoria=producto.categoria
    ).exclude(pk=producto.pk)[:3]  # mostramos hasta 3

    return render(
        request,
        'tienda/detalle_producto.html',
        {
            'producto': producto,
            'relacionados': relacionados
        }
    )


def todos_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/todos_productos.html', {'productos': productos})
