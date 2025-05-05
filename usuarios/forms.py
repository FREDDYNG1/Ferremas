from django import forms
from django.contrib.auth.models import User
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate



class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        email = self.cleaned_data['email']
        user.username = email  # Usamos el email como nombre de usuario
        user.email = email
        if commit:
            user.save()
        return user


class UsuarioExtraForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['fecha_nacimiento', 'telefono', 'direccion']


class CrearTrabajadorForm(forms.ModelForm):
    email = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    nombre = forms.CharField(label='Nombre')
    apellido = forms.CharField(label='Apellido')

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'telefono', 'fecha_nacimiento', 'direccion']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['nombre'],
            last_name=self.cleaned_data['apellido'],
            password=self.cleaned_data['password']
        )
        usuario = super().save(commit=False)
        usuario.user = user
        usuario.rol = 'trabajador'
        if commit:
            user.save()
            usuario.save()
        return usuario
class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(attrs={'autofocus': True}))

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        try:
            user = User.objects.get(email=email)
            self.cleaned_data['username'] = user.username  # asignamos el username real
        except User.DoesNotExist:
            raise ValidationError("Correo electrónico o contraseña inválidos")

        return super().clean()
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Ya existe un usuario con este correo electrónico.")
        return email
