from django.shortcuts import render, redirect
from tienda.models import Producto
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm, UserForm
from .models import Profile

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

def como_comprar(request):
    return render(request, "como_comprar.html")

@login_required
def mi_cuenta(request):
    return render(request, "account/mi_cuenta.html")


@login_required
def edit_profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        profile_form = EditProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("mi_cuenta")
    else:
        user_form = UserForm(instance=user)
        profile_form = EditProfileForm(instance=profile)

    return render(request, "account/edit_profile.html", {
        "user_form": user_form,
        "profile_form": profile_form,
    })

