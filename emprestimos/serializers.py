from emprestimos.models import Emprestimo
from rest_framework import serializers

class EmprestimosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = '__all__'