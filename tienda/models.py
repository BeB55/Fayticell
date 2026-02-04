from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    destacado = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)  # nuevo campo

    def __str__(self):
        return self.nombre

    @property
    def disponible(self):
        return self.stock > 0
