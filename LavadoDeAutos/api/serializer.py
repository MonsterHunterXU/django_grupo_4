from LavadoAutos.models import Insumos, Contacto
from rest_framework import serializers

#Modelo a Serealizar
class InsumoSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Insumos
        fields = ["cod","nombreinsumo","precio","descripcion","stock"]

class ContactoSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ["cod","name","lastname","asunto","tipoContacto","mensaje"]
        