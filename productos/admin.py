from django.contrib import admin
from productos.models import Producto , Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'stock', 'creado']
    search_fields = ['nombre']
    list_filter = ['categoria', 'creado']