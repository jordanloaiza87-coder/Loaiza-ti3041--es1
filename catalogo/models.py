from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.URLField(max_length=500, blank=True, null=True) # Campo nuevo para la imagen

    def __str__(self):
        return self.nombre