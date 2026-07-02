# Sangre y Ceniza

Sangre y Ceniza es una aplicación web tipo e-commerce inspirada en la estética y el legado de las culturas vikinga, sajona y normanda. La plataforma simula una tienda especializada en réplicas de grado museo — armas, armaduras y accesorios medievales — pensada como vitrina para coleccionistas y entusiastas de la historia antigua.

## Autor

Nahib Mubaharak Aliaga


## Objetivo del proyecto

Desarrollar una aplicación e-commerce funcional el cual integra autenticación con roles, gestión de catálogo mediante el ORM, y un flujo completo de compra (carrito → confirmación → orden), aplicando buenas prácticas de estructura, persistencia de datos y validaciones,desarrollado con Django como proyecto final del Bootcamp Python2026.

##  Repositorio

https://github.com/Xiihib/sangre_y_ceniza.git

## 🚀 Tecnologías

- Python 3.14
- Django 6.0
- SQLite
- Bootstrap 5


## Requisitos 

Leer requirements.txt

##  Instalación

### Descargar el repositorio
```bash
git clone https://github.com/Xiihib/sangre_y_ceniza.git
cd sangre_y_ceniza
```



### Crear y activar un entorno virtual:
```bash
python -m venv venv
source venv/scripts/activate
```

### Instalar las dependencias:
```bash
pip install -r requirements.txt
```

### Implementar las migraciones:
```bash
python manage.py migrate
```
### Correr el servidor:
```bash
python manage.py runserver
```

### Abrir el navegador:
```
http://127.0.0.1:8000/
```
## Rutas principales

| Ruta                          | Descripción                     | Acceso      |
|-------------------------------|----------------------------------|-------------|
| `/`                           | Página de inicio (La Gran Sala) | Público     |
| `/productos/`                 | Catálogo de productos           | Público     |
| `/productos/<id>/`            | Detalle de producto             | Público     |
| `/productos/crear/`           | Crear producto                  | Admin       |
| `/productos/<id>/editar/`     | Editar producto                 | Admin       |
| `/productos/<id>/eliminar/`   | Eliminar producto                | Admin       |
| `/usuarios/login/`            | Iniciar sesión                  | Público     |
| `/usuarios/registro/`         | Crear cuenta                    | Público     |
| `/usuarios/logout/`           | Cerrar sesión                   | Autenticado |
| `/pedidos/carrito/`           | Ver carrito                     | Cliente     |
| `/pedidos/carrito/confirmar/` | Confirmar compra                | Cliente     |
| `/pedidos/orden/<id>/`        | Detalle de orden                | Cliente     |
| `/pedidos/orden/<id>/pagar/`  | Pagar orden (simulado)          | Cliente     |
| `/admin/`                     | Panel de administración Django  | Admin       |

##  Credenciales de prueba

Administrador
- Usuario: `admin`
- Contraseña: `admin`

Cliente
- Usuario: `usuario`
- Contraseña: `usuario`

## Funcionalidades

- Autenticación con roles (admin / cliente) usando `is_staff`
- CRUD completo de productos (solo admin)
- Catálogo de productos persistido en base de datos (ORM de Django)
- Carrito de compras: agregar, quitar, actualizar cantidades, subtotales y total
- Confirmación de compra: genera una orden asociada al usuario autenticado
- Simulación de pago: genera un código de transacción y actualiza el estado de la orden a "Pagada"
- Validaciones en formularios (campos requeridos, precio > 0, stock > 0)
- Mensajes claros de éxito/error en toda la aplicación

