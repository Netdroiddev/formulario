# utils.py
import os
from django.utils.text import slugify
from datetime import datetime

def ruta_firma_personalizada(instance, filename):
    nombre = slugify(instance.nombre_completo)
    extension = filename.split('.')[-1]
    nuevo_nombre = f"firma_{datetime.now().strftime('%Y%m%d%H%M%S')}.{extension}"
    return os.path.join('firmas', nombre, nuevo_nombre)
