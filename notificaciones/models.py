from django.db import models

class Fotocopiadora(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=150)
    estado = models.CharField(
        max_length=20, 
        choices=[('activo', 'Activo'), ('inactivo', 'Inactivo'), ('mantenimiento', 'Mantenimiento')],
        default='activo'
    )
    contador_impresiones = models.IntegerField(default=0)
    toner_actual = models.IntegerField(default=100)  # % de tóner
    ultima_revision = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.modelo} ({self.marca})"


class Notificacion(models.Model):
    fotocopiadora = models.ForeignKey('Fotocopiadora', on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)  # Asegúrate de que existe este campo
    estado = models.CharField(
        max_length=20,
        choices=[('pendiente', 'Pendiente'), ('resuelta', 'Resuelta')],
        default='pendiente'
    )


    def __str__(self):
        return f"Notificación: {self.mensaje} ({self.fotocopiadora.modelo})"

class Tecnico(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Mantenimiento(models.Model):
    fotocopiadora = models.ForeignKey('Fotocopiadora', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('completado', 'Completado')])

    def __str__(self):
        return f"{self.fotocopiadora} - {self.estado}"

