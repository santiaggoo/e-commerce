Este proyecto es una tienda online desarrollada con Python y el framework Django,
Permite a los usuarios navegar productos, agregarlos al carrito, realizar compras y gestionar pedidos.

Funcionalidades principales
- Catálogo de productos con categorías
- Carrito de compras dinámico
- Procesamiento de pedidos
- Panel de administración para gestión de productos y usuarios
🛠️ Tecnologías utilizadas
- Python 
- Django
- SQLite 
- HTML, CSS
- Django Admin para gestión interna

 Instalación del proyecto
1. Clonar el repositorio
git clone https://github.com/santiaggoo/e-commerce.git

2. Crear y activar un entorno virtual
python -m venv env
source env/bin/activate  # En Linux/macOS
env\Scripts\activate     # En Windows

3. Instalar dependencias
pip install -r requirements.txt

4. Configurar la base de datos
python manage.py migrate


5. Crear un superusuario para acceder al panel de administración
python manage.py createsuperuser


Se te pedirá que ingreses un nombre de usuario, correo electrónico y contraseña. Guarda estos datos, ya que los necesitarás para ingresar al panel de administración.

6. Ejecutar el servidor
python manage.py runserver


Luego abre tu navegador y accede a:
📍 http://127.0.0.1:8000/admin/

🧑‍💼 Uso del panel de administración
Una vez que ingreses con el superusuario que creaste, podrás:
- Agregar productos
- Crear categorías
- Editar o eliminar registros existentes

Luego de agregar las categorias accede a:
http://127.0.0.1:8000 para ingresar al inicio de la tienda



