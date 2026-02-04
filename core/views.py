from django.shortcuts import render, redirect, get_object_or_404
from core.models import Producto
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EditProfileForm, UserForm
from .models import Profile
from django.http import HttpResponse
from django.conf import settings
import mercadopago


def home(request):
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

def como_comprar(request):
    return render(request, "como_comprar.html")

def productos(request):
    productos = Producto.objects.all()
    categoria = request.GET.get('categoria')

    if categoria:
        productos = productos.filter(categoria__iexact=categoria)

    query = request.GET.get('q')
    if query:
        productos = productos.filter(nombre__icontains=query)

    return render(request, 'productos.html', {'productos': productos})

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


def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})

def agregar_al_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    producto = get_object_or_404(Producto, id=producto_id)

    if str(producto_id) in carrito:
        carrito[str(producto_id)]['cantidad'] += 1
    else:
        carrito[str(producto_id)] = {
            'nombre': producto.nombre,
            'precio': float(producto.precio),
            'cantidad': 1,
            'imagen': producto.imagen.url if producto.imagen else None,
        }

    request.session['carrito'] = carrito
    return redirect(request.META.get('HTTP_REFERER', 'productos'))

def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    if str(producto_id) in carrito:
        del carrito[str(producto_id)]
        request.session['carrito'] = carrito
    return redirect('carrito')

def incrementar_cantidad(request, producto_id):
    carrito = request.session.get('carrito', {})
    if str(producto_id) in carrito:
        carrito[str(producto_id)]['cantidad'] += 1
        request.session['carrito'] = carrito
    return redirect(request.META.get('HTTP_REFERER', 'carrito'))

def disminuir_cantidad(request, producto_id):
    carrito = request.session.get('carrito', {})
    if str(producto_id) in carrito:
        if carrito[str(producto_id)]['cantidad'] > 1:
            carrito[str(producto_id)]['cantidad'] -= 1
        else:
            carrito.pop(str(producto_id))
        request.session['carrito'] = carrito
    return redirect(request.META.get('HTTP_REFERER', 'carrito'))


def checkout(request):
    if request.method == "POST":
        metodo = request.POST.get("metodo_pago")

        if metodo == "efectivo":
            return redirect("pago_exito")

        elif metodo == "tarjeta":
            sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)

            preference_data = {
                "items": [
                    {
                        "title": "Compra Fayticell",
                        "quantity": 1,
                        "currency_id": "ARS",
                        "unit_price": 100.00
                    }
                ],
                "back_urls": {
                    "success": "https://fayticell.onrender.com/pago/exito/",
                    "failure": "https://fayticell.onrender.com/pago/error/",
                    "pending": "https://fayticell.onrender.com/pago/pendiente/"
                },
                "auto_return": "approved",
            }

            preference_response = sdk.preference().create(preference_data)
            preference = preference_response["response"]

            return redirect(preference["init_point"])

        return render(request, "checkout.html", {"error": "Seleccioná un método de pago"})

    return render(request, "checkout.html")


def iniciar_pago(request):
    sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)

    preference_data = {
        "items": [
            {
                "title": "Producto ejemplo",
                "quantity": 1,
                "currency_id": "ARS",
                "unit_price": 1500.00
            }
        ],
        "back_urls": {
            "success": "https://fayticell.onrender.com/pago/exito/",
            "failure": "https://fayticell.onrender.com/pago/error/",
            "pending": "https://fayticell.onrender.com/pago/pendiente/"
        },
        "auto_return": "approved",
    }

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]

    return redirect(preference["init_point"])

def pago_exito(request):
     return HttpResponse("Pago realizado con éxito ✅") 

def pago_error(request):
     return HttpResponse("Hubo un error en el pago ❌")
     
def pago_pendiente(request):
    return HttpResponse("El pago está pendiente ⏳")
