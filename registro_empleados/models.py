from django.db import models
from .utils import ruta_firma_personalizada


class Empleado(models.Model):
    TIPO_DOCUMENTO = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('Pasaporte', 'Pasaporte'),
    ]
    
    JORNADA_CHOICES = [
        ('Completa', 'Jornada completa'),
        ('Mañana', 'Mañana'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
    ]
    
    DIAS_CHOICES = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]

    nombre_completo = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=20, choices=TIPO_DOCUMENTO)
    numero_documento = models.CharField(max_length=20)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    cargo = models.CharField(max_length=100)
    tp_rm = models.CharField(max_length=100, blank=True, null=True)
    firma = models.ImageField(upload_to=ruta_firma_personalizada, blank=True, null=True)
    dias_laborales = models.CharField(max_length=100)
    jornada = models.CharField(max_length=20, choices=JORNADA_CHOICES)

    def __str__(self):
        return self.nombre_completo

    def save(self, *args, **kwargs):
        # Personalizar el guardado de la firma
        if self.pk:
            old_instance = Empleado.objects.get(pk=self.pk)
            if old_instance.firma and old_instance.firma != self.firma:
                old_instance.firma.delete(save=False)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'Empleado'  # Aquí se define explícitamente el nombre de la tabla
