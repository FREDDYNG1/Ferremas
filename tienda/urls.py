from django.urls import path
from .views import vista_productos_cliente
from tienda.views import agregar_producto  # Asegúrate de importar agregar_producto desde views.py
from tienda.views import ver_pedidos  # Asegúrate de importar ver_pedidos desde views.py

urlpatterns = [
    path('catalogo/', vista_productos_cliente, name='vista_productos_cliente'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),  # Asegúrate de importar agregar_producto desde views.py
    path('pedidos/', ver_pedidos, name='ver_pedidos'), 
]
