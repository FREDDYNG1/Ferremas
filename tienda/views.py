from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import Producto
from usuarios.models import Usuario

def vista_productos_cliente(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/productos_cliente.html', {'productos': productos})

@login_required
def agregar_producto(request):
    usuario = Usuario.objects.get(user=request.user)
    if usuario.rol != 'trabajador':
        return redirect('home')

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vista_productos_cliente')
    else:
        form = ProductoForm()

    return render(request, 'tienda/agregar_producto.html', {'form': form})
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@login_required
@never_cache
def ver_pedidos(request):
    return render(request, 'tienda/ver_pedidos.html')
