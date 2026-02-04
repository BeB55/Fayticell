from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"


class Producto(models.Model):
    CATEGORIAS = [
        ("celulares", "Celulares"),
        ("accesorios", "Accesorios"),
        ("repuestos", "Repuestos"),
        ("servicios", "Servicios"),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    destacado = models.BooleanField(default=False)   # 👈 este campo faltaba
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default="celulares")

    def __str__(self):
        return self.nombre

