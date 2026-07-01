from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField( default="Sin descripcion")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']

class Producto(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, blank=True, null=True)
    descripcion = models.TextField(default="Sin descripcion")
    precio = models.DecimalField(max_digits=10 ,decimal_places=2, validators=[MinValueValidator(0.01)])
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']