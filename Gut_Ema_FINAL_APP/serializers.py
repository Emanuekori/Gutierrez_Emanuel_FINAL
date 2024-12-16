from rest_framework import serializers
from .models import Inscrito, Institucion

class InscritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscrito
        fields = ['id', 'institucion', 'nombre', 'nro_personas', 'telefono', 'fecha_inscripcion', 'hora_inscripcion', 'estado', 'observacion']

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = ['id', 'nombre']
