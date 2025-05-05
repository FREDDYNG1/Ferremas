from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    ROLES = (
        ('cliente', 'Cliente'),
        ('trabajador', 'Trabajador'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    rol = models.CharField(max_length=20, choices=ROLES, default='cliente')

    def __str__(self):
        return f"{self.user.username} - {self.rol}"
