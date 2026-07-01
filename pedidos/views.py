from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .models import Carrito, ItemCarrito, Orden, ItemOrden
from productos.models import Producto


@login_required
def ver_carrito(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.all()
    total = sum(item.subtotal() for item in items)
    return render(request, 'pedidos/carrito.html', {'items': items, 'total': total})


@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)

    item, item_creado = ItemCarrito.objects.get_or_create(
        carrito=carrito,
        producto=producto,
        defaults={'precio_unitario': producto.precio}
    )

    if not item_creado:
        item.cantidad += 1
        item.save()

    messages.success(request, f'{producto.nombre} agregado al carrito')
    return redirect('productos:detalle', id=producto.id)


@login_required
def actualizar_cantidad(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__usuario=request.user)

    if request.method == 'POST':
        try:
            nueva_cantidad = int(request.POST['cantidad'])
            if nueva_cantidad < 1:
                messages.warning(request, 'La cantidad debe ser mayor a 0')
            else:
                item.cantidad = nueva_cantidad
                item.save()
                messages.success(request, 'Cantidad actualizada')
        except (ValueError, KeyError):
            messages.error(request, 'Cantidad inválida')

    return redirect('pedidos:ver_carrito')


@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__usuario=request.user)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Producto eliminado del carrito')
    return redirect('pedidos:ver_carrito')

@login_required
def confirmar_compra(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.all()

    if not items.exists():
        messages.warning(request, 'Tu carrito está vacío')
        return redirect('pedidos:ver_carrito')

    total = sum(item.subtotal() for item in items)

    with transaction.atomic():
        orden = Orden.objects.create(usuario=request.user, total=total)
        for item in items:
            ItemOrden.objects.create(
                orden=orden,
                producto=item.producto,
                nombre_producto=item.producto.nombre,
                cantidad=item.cantidad,
                precio_unitario=item.precio_unitario
            )
        items.delete()

    messages.success(request, f'¡Compra confirmada! Orden #{orden.id}')
    return redirect('pedidos:ver_carrito')