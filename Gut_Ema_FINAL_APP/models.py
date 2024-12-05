from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=80, unique=True, verbose_name="Nombre de la Institución")

    def __str__(self):
        return self.nombre

class Inscrito(models.Model):
    ESTADO_CHOICES = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, verbose_name="Institución")
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Inscrito")
    nro_personas = models.PositiveSmallIntegerField(verbose_name="Número de Personas")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono de Contacto")
    fecha_inscripcion = models.DateField(auto_now_add=True, verbose_name="Fecha de Inscripción")
    hora_inscripcion = models.TimeField(auto_now_add=True, verbose_name="Hora de Inscripción")
    estado = models.CharField(max_length=12, choices=ESTADO_CHOICES, default='RESERVADO', verbose_name="Estado")
    observacion = models.TextField(blank=True, null=True, verbose_name="Observación")

    def __str__(self):
        return f"{self.nombre} ({self.institucion.nombre})"
