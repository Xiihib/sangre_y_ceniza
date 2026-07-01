from django.urls import path
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('registro/', views.registro, name='registro'),
]