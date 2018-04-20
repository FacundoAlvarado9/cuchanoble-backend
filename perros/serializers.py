# Importando liberias del framework
from rest_framework import serializers
# Importando el modelo
from .models import Perro

#Creando el serializer (traduce de un modelo a JSON)
class PerroSerializer(serializers.ModelSerializer):
    #De donde vamos a sacar el modelo
    class Meta:
        model = Perro
        fields = ('direccion', 'sexo', 'edad', 'tamano', 'estado', 'contacto', 'imagen')
