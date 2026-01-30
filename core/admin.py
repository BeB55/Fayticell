from django.contrib import admin
from .models import Producto, Profile

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio')
    list_filter = ('categoria',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefono', 'direccion')
