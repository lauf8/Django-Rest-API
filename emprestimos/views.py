from django.shortcuts import render

from emprestimos.models import Emprestimo
from emprestimos.serializers import EmprestimosSerializers
from rest_framework import generics

class EmprestimoListar(generics.ListAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimosSerializers

class EmprestimoCriar(generics.CreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimosSerializers

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
