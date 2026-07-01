from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar'),
    path('carrito/actualizar/<int:item_id>/', views.actualizar_cantidad, name='actualizar'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar'),
    path('carrito/confirmar/', views.confirmar_compra, name='confirmar'),
]