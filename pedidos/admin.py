from django.contrib import admin
from .models import Carrito, ItemCarrito, Orden, ItemOrden


class ItemCarritoInline(admin.TabularInline):
    model = ItemCarrito
    extra = 0


@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'creado']
    inlines = [ItemCarritoInline]


class ItemOrdenInline(admin.TabularInline):
    model = ItemOrden
    extra = 0


@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'fecha', 'total', 'estado']
    list_filter = ['estado', 'fecha']
    inlines = [ItemOrdenInline]