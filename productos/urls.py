from django.urls import path
from productos import views


app_name = 'productos'

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.listar, name='listar'),
    path('productos/crear/', views.crear, name='crear'),
    path('productos/<int:id>/', views.detalle, name='detalle'),
    path('productos/<int:id>/editar/', views.editar, name='editar'),
    path('productos/<int:id>/eliminar/', views.eliminar, name='eliminar'),
]