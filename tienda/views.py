from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.contrib import messages
from core.models import Producto
from core.forms import ProductoForm
import pandas as pd

def inicio(request):
    return HttpResponse("Bienvenido a Fayticell - Tu servicio tecnico de confianza.")

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    # Buscar productos relacionados por categoría
    relacionados = Producto.objects.filter(
        categoria=producto.categoria
    ).exclude(pk=producto.pk)[:3]

    # Obtener cantidad actual en el carrito
    carrito = request.session.get('carrito', {})
    cantidad_en_carrito = carrito.get(str(producto.id), {}).get('cantidad', 0)

    return render(
        request,
        'tienda/detalle_producto.html',
        {
            'producto': producto,
            'relacionados': relacionados,
            'cantidad_en_carrito': cantidad_en_carrito,
        }
    )

def todos_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/todos_productos.html', {'productos': productos})

@user_passes_test(lambda u: u.is_staff)
def agregar_producto(request):
    if request.method == 'POST':
        # ✅ Caso: carga masiva desde Excel
        if "import_excel" in request.POST and "excel_file" in request.FILES:
            excel_file = request.FILES["excel_file"]
            try:
                df = pd.read_excel(excel_file)

                for _, row in df.iterrows():
                    Producto.objects.create(
                        nombre=row.get("nombre", ""),
                        descripcion=row.get("descripcion", ""),
                        precio=row.get("precio", 0),
                        destacado=row.get("destacado", False),
                        # Si tu modelo tiene categoría, podés mapearla también
                        # categoria_id=row.get("categoria_id", None),
                    )
                messages.success(request, "📥 Productos importados correctamente desde Excel.")
                return redirect('tienda:todos_productos')
            except Exception as e:
                messages.error(request, f"❌ Error al procesar el Excel: {e}")
                form = ProductoForm()
                return render(request, 'tienda/agregar_producto.html', {'form': form})

        # ✅ Caso: creación manual con formulario
        else:
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "✅ Producto agregado correctamente.")
                return redirect('tienda:todos_productos')
            else:
                messages.error(request, "❌ Error al agregar el producto. Revisá los campos.")
    else:
        form = ProductoForm()
    return render(request, 'tienda/agregar_producto.html', {'form': form})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "✏️ Producto editado correctamente.")
            return redirect("tienda:todos_productos")
        else:
            messages.error(request, "❌ Error al editar el producto. Revisá los campos.")
    else:
        form = ProductoForm(instance=producto)
    return render(request, "tienda/editar_producto.html", {"form": form, "producto": producto})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        producto.delete()
        messages.success(request, "🗑️ Producto eliminado correctamente.")
        return redirect("tienda:todos_productos")
    return render(request, "tienda/eliminar_producto.html", {"producto": producto})
