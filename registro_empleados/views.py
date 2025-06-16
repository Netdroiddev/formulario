# views.py
from django.shortcuts import render, redirect
from .forms import EmpleadoForm
from django.contrib import messages

def registro_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            empleado = form.save(commit=False)
            # Convertir lista de días a string separado por comas
            empleado.dias_laborales = ', '.join(form.cleaned_data['dias_laborales'])
            empleado.save()
            messages.success(request, '¡Informacion guardada exitosamente!')
            return redirect('registro_empleado')
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = EmpleadoForm()
    
    return render(request, 'index.html', {'form': form})


