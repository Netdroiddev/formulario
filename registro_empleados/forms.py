from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    DIAS_CHOICES = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]
    
    dias_laborales = forms.MultipleChoiceField(
        choices=DIAS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'jornada': forms.RadioSelect,
        }

    def clean(self):
        cleaned_data = super().clean()
        cargo = cleaned_data.get('cargo', '').lower()
        firma = cleaned_data.get('firma')

        # Solo exigir firma si el cargo contiene términos relacionados con salud
        es_profesional_salud = any(palabra in cargo for palabra in ['doctor', 'médico', 'medico', 'enfermero', 'salud'])

        if es_profesional_salud and not firma:
            self.add_error('firma', "Este campo es obligatorio para profesionales de la salud.")

        return cleaned_data

    def clean_firma(self):
        firma = self.cleaned_data.get('firma')
        if firma:
            # Validar tipo de archivo
            if not firma.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise forms.ValidationError("Formato no válido. Use PNG, JPG o JPEG.")
            # Validar tamaño (máximo 2MB)
            if firma.size > 2 * 1024 * 1024:
                raise forms.ValidationError("La imagen es demasiado grande (máximo 2MB).")
        return firma
