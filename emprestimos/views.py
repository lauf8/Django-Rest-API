from django.shortcuts import render
from emprestimos.models import Emprestimo
from objetos.models import Objetos
from emprestimos.serializers import EmprestimosSerializers
from rest_framework import generics

class EmprestimoListar(generics.ListAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimosSerializers

class EmprestimoCriar(generics.CreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimosSerializers

    def perform_create(self, serializer):
        objetos_disponiveis = Objetos.objects.filter(status='disponivel')
        objetos_emprestimo = []

        for objeto in objetos_disponiveis:
            objetos_emprestimo.append(objeto.id)
        serializer.save(objeto_emprestimo=objetos_emprestimo)
        
class EmprestimoAtualizar(generics.UpdateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimosSerializers
    lookup_field = 'id'

class EmprestimoDetalhar(generics.RetrieveAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimosSerializers
    lookup_field = 'id'

class EmprestimoApagar(generics.DestroyAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimosSerializers
    lookup_field = 'id'
