from django.urls import path
from .views import home, vista_admin, crear_trabajador
from . import views
from django.contrib.auth import views as auth_views
from .forms import EmailAuthenticationForm

urlpatterns = [
    path('home/', home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('cliente/', views.home_cliente, name='home_cliente'),
    path('trabajador/', views.home_trabajador, name='home_trabajador'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',authentication_form=EmailAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('admin-panel/', vista_admin, name='vista_admin'),
    path('crear-trabajador/', crear_trabajador, name='crear_trabajador'),
    path('redirigir/', views.redirigir_usuario, name='redirigir_usuario'),  
]
