from rest_framework import serializers
from .models import Emprendimiento, Emprendedor,Servicio

class EmprendimientoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Emprendimiento
        fields= '__all__'

class EmprendedorSerializers(serializers.ModelSerializer):
    class Meta:
        model= Emprendedor
        fields= '__all__'

class ServicioSerializers(serializers.ModelSerializer):
    class Meta:
        model=Servicio
        fields='__all__'
