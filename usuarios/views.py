from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido, {user.username}')
            return redirect('productos:listar')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return render(request, 'usuarios/login.html')
    return render(request, 'usuarios/login.html')

def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Sesión cerrada correctamente')
    return redirect('productos:listar')

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if not username or not password:
            messages.warning(request, 'Usuario y contraseña son obligatorios')
            return render(request, 'usuarios/registro.html')

        if password != password2:
            messages.warning(request, 'Las contraseñas no coinciden')
            return render(request, 'usuarios/registro.html')

        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Ese nombre de usuario ya existe')
            return render(request, 'usuarios/registro.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, 'Cuenta creada exitosamente')
        return redirect('productos:listar')

    return render(request, 'usuarios/registro.html')