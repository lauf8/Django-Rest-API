from app.models import Locador
from rest_framework import serializers

class LocadorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Locador
        fields = '__all__'