from django.urls import path
from . import views

urlpatterns = [
    path('', views.registro_empleado, name='registro_empleado'),  # Usa la vista que maneja el formulario
]
