from objetos.models import Objetos
from rest_framework import serializers

class ObjetosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Objetos
        fields = '__all__'

class ObjetosSerializersCreate(serializers.ModelSerializer):
    class Meta:
        model = Objetos
        fields = 'estado', 'tipo', 'observacao', 'status'

    