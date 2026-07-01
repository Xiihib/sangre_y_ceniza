from django.shortcuts import render , redirect , get_object_or_404
from productos.models import Categoria, Producto
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

def es_staff(user):
    return user.is_staff

def index(request):
    productos = Producto.objects.all()
    return render(request, 'productos/index.html', {'productos': productos})

def listar(request):
    producto = Producto.objects.all()
    return render(request, 'productos/listar.html', {"producto":producto})

@user_passes_test(es_staff)
def crear(request):
    categorias = Categoria.objects.all()
    if request.method == "POST":
        nombre = request.POST['nombre']
        if not nombre:
            messages.warning(request, "El nombre es obligatorio")
            return render(request, 'productos/crear.html', {"categorias": categorias})
        categoria_id = request.POST ['categoria']
        categoria = Categoria.objects.get(id=categoria_id)
        descripcion = request.POST ['descripcion']
        precio =  request.POST ['precio']
        if not precio:
            messages.warning(request, "El precio es obligatorio")
            return render(request, 'productos/crear.html', {"categorias": categorias})
        precio = float(precio)
        if precio <= 0:
            messages.warning(request, "El precio debe ser mayor a cero")
            return render(request, 'productos/crear.html', {"categorias": categorias})
        stock = request.POST ['stock']
        if not stock:
            messages.warning(request, "El stock es obligatorio")
            return render(request, 'productos/crear.html', {"categorias": categorias})
        stock = int(stock)
        if stock <= 0:
            messages.warning(request, "El stock no puede ser negativo")
            return render(request, 'productos/crear.html', {"categorias": categorias})
        imagen = request.FILES.get('imagen')
        Producto.objects.create(nombre=nombre , categoria=categoria, descripcion=descripcion, precio=precio,stock=stock, imagen=imagen)
        messages.success(request,"Producto creado")
        return redirect('productos:listar')
    return render(request, 'productos/crear.html', {"categorias": categorias})

@user_passes_test(es_staff)
def editar(request, id):
    producto = get_object_or_404(Producto, id=id)
    categorias = Categoria.objects.all()
    if request.method == "POST":
        producto.nombre = request.POST['nombre']
        if not producto.nombre:
            messages.warning(request, "El nombre es obligatorio")
            return render(request, 'productos/editar.html', {'categorias':categorias,"producto":producto})
        categoria_id = request.POST ['categoria']
        categoria = get_object_or_404(Categoria, id=categoria_id)
        producto.categoria = categoria
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        if not producto.precio:
            messages.warning(request, "El precio es obligatorio")
            return render(request, 'productos/editar.html', {'categorias':categorias,"producto":producto})
        producto.precio = float(producto.precio)
        if producto.precio <= 0:
            messages.warning(request, "El precio debe ser mayor a cero")
            return render(request, 'productos/editar.html', {'categorias':categorias,"producto":producto})
        producto.stock = request.POST['stock']
        if not producto.stock:
            messages.warning(request, "El stock es obligatorio")
            return render(request, 'productos/editar.html', {'categorias':categorias,"producto":producto})
        producto.stock = int(producto.stock)
        if producto.stock <= 0:
            messages.warning(request, "El stock no puede ser negativo")
            return render(request, 'productos/editar.html', {'categorias':categorias,"producto":producto})
        if 'imagen' in request.FILES:
            producto.imagen = request.FILES['imagen']
        producto.save()
        messages.success(request,"Producto actualizado")
        return redirect('productos:listar')
    return render (request, 'productos/editar.html', {'categorias':categorias,"producto":producto} )

@user_passes_test(es_staff)
def eliminar(request,id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.delete()
        messages.success(request, "Producto eliminado")
        return redirect('productos:listar')
    return render(request, 'productos/eliminar.html', {'producto': producto})
    

def detalle(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'productos/detalle.html', {'producto': producto})