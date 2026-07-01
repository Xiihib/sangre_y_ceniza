# Sangre y Ceniza

E-commerce de réplicas vikingas, sajonas y normandas de grado museo, 

## Objetivo del proyecto

Desarrollar una aplicación e-commerce funcional el cual integra autenticación con roles, gestión de catálogo mediante el ORM, y un flujo completo de compra (carrito → confirmación → orden), aplicando buenas prácticas de estructura, persistencia de datos y validaciones,desarrollado con Django como proyecto final del Bootcamp Python2026.

## Autor

Nahib

##  Repositorio

https://github.com/Xiihib/sangre_y_ceniza.git

## Requisitos 

Leer requirements.txt

##  Instalación

### Descargar el repositorio
bash
git clone https://github.com/Xiihib/sangre_y_ceniza.git
cd sangre_y_ceniza




### Crear y activar un entorno virtual:
bash
python -m venv venv
source venv/scripts/activate

### Instalar las dependencias:
bash
pip install -r requirements.txt


### Implementar las migraciones:
bash
python manage.py migrate

### Correr el servidor:
bash
python manage.py runserver


### Abrir el navegador:
http://127.0.0.1:8000/

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
| `/admin/`                     | Panel de administración Django  | Admin       |

##  Credenciales de prueba

Administrador
- Usuario: `admin`
- Contraseña: `admin`

Cliente
- Usuario: `usuario`
- Contraseña: `usuario`
