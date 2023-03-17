from emprestimos.models import Emprestimo
from rest_framework import serializers
from objetos.serializers import ObjetosSerializers

class EmprestimosSerializers(serializers.ModelSerializer):

    class Meta:

        model = Emprestimo
        fields = '__all__'
   