from django.shortcuts import render
from objetos.models import Objetos
from objetos.serializers import ObjetosSerializers, ObjetosSerializersCreate
from rest_framework import generics
from helpers.random import gerar_caracteres_aleatorios

class ObjetosListar(generics.ListAPIView):
    queryset = Objetos.objects.all()
    serializer_class = ObjetosSerializers

class ObjetosCriar(generics.CreateAPIView):
    queryset = Objetos.objects.all()
    serializer_class = ObjetosSerializersCreate

class ObjetosAtualizar(generics.UpdateAPIView):
    queryset = Objetos.objects.all()
    serializer_class = ObjetosSerializers
    lookup_field = 'id'

class ObjetosDetalhar(generics.RetrieveAPIView):
    queryset = Objetos.objects.all()
    serializer_class = ObjetosSerializers
    lookup_field = 'id'

class ObjetosApagar(generics.DestroyAPIView):
    queryset = Objetos.objects.all()
    serializer_class = ObjetosSerializers
    lookup_field = 'id'