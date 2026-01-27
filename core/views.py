from django.shortcuts import render
from tienda.models import Producto   

def home(request):
    # Trae los productos destacados (máximo 6)
    productos = Producto.objects.filter(destacado=True)[:6]
    return render(request, 'home.html', {'productos': productos})

def garantias(request):
    return render(request, 'garantias.html')

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')

def nosotros(request):
    return render(request, 'nosotros.html')

from django.core.mail import send_mail
from django.http import HttpResponse

def test_email(request):
    send_mail(
        subject="Prueba de correo desde Fayticell",
        message="Hola Brian, este es un correo de prueba enviado con Brevo SMTP.",
        from_email="Fayticell <brianebaptista@gmail.com>",  # remitente verificado en Brevo
        recipient_list=["brianebaptista@gmail.com"],         # destinatario de prueba
        fail_silently=False,
    )
    return HttpResponse("✅ Correo de prueba enviado.")
