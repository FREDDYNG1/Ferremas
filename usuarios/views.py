from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CrearTrabajadorForm, RegistroUsuarioForm, UsuarioExtraForm
from .models import Usuario

@never_cache
def home(request):
    contexto = {}

    if request.user.is_authenticated:
        try:
            usuario = Usuario.objects.get(user=request.user)
            contexto['rol'] = usuario.rol
        except Usuario.DoesNotExist:
            contexto['rol'] = 'admin' if request.user.is_superuser else 'sin_rol'
        contexto['usuario'] = request.user

    return render(request, 'home.html', contexto)


def registro(request):
    if request.method == 'POST':
        form_user = RegistroUsuarioForm(request.POST)
        form_usuario = UsuarioExtraForm(request.POST)
        if form_user.is_valid() and form_usuario.is_valid():
            user = form_user.save()
            usuario = form_usuario.save(commit=False)
            usuario.user = user
            usuario.rol = 'cliente'  # Seguridad: todos los registros son clientes
            usuario.save()
            login(request, user)

            return redirect('redirigir_usuario')
    else:
        form_user = RegistroUsuarioForm()
        form_usuario = UsuarioExtraForm()

    return render(request, 'registro.html', {
        'form_user': form_user,
        'form_usuario': form_usuario
    })


@login_required
@never_cache
def redirigir_usuario(request):
    try:
        usuario = Usuario.objects.get(user=request.user)
        if request.user.is_superuser:
            return redirect('/admin/')
        elif request.user.is_staff:
            return redirect('vista_admin')
        elif usuario.rol == 'cliente':
            return redirect('home_cliente')
        elif usuario.rol == 'trabajador':
            return redirect('home_trabajador')
    except Usuario.DoesNotExist:
        if request.user.is_superuser:
            return redirect('/admin/')
        elif request.user.is_staff:
            return redirect('vista_admin')
        else:
            return redirect('home')


@login_required
@never_cache
def home_cliente(request):
    return render(request, 'home_cliente.html')


@login_required
@never_cache
def home_trabajador(request):
    return render(request, 'home_trabajador.html')


@staff_member_required
@never_cache
def crear_trabajador(request):
    if request.method == 'POST':
        form = CrearTrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vista_admin')
    else:
        form = CrearTrabajadorForm()

    return render(request, 'crear_trabajador.html', {'form': form})


@staff_member_required
@never_cache
def vista_admin(request):
    return render(request, 'vista_admin.html')
