from django import forms
from .models import Inscrito, Institucion

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre de la Institución',
        }
        
class InscritoForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = ['institucion', 'nombre', 'nro_personas', 'telefono', 'estado', 'observacion']
        labels = {
            'institucion': 'Institución',
            'nombre': 'Nombre del Inscrito',
            'nro_personas': 'Número de Personas',
            'telefono': 'Teléfono de Contacto',
            'estado': 'Estado de la Inscripción',
            'observacion': 'Observación (Opcional)',
        }

    def clean_nro_personas(self):
        nro_personas = self.cleaned_data['nro_personas']
        if nro_personas < 1 or nro_personas > 30:
            raise forms.ValidationError("El número de personas debe estar entre 1 y 30.")
        return nro_personas

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) > 80:
            raise forms.ValidationError("El nombre de la institución no debe superar los 80 caracteres.")
        return nombre
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not telefono.isdigit() or len(telefono) < 8:
            raise forms.ValidationError("El teléfono debe ser un número válido de al menos 8 dígitos.")
        return telefono
