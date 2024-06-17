from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to='fotos_empleados/', blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
