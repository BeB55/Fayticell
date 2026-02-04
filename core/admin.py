from django.contrib import admin
from .models import Producto, Profile

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'destacado')  # columnas visibles
    list_editable = ('stock',)  # permite editar stock directamente en la lista
    search_fields = ('nombre',)
    list_filter = ('categoria', 'destacado')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefono', 'direccion')
