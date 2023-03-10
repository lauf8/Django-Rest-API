from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Locador
from rest_framework import status
from rest_framework import generics
from app.serializers import LocadorSerializers


class LocadorListar(generics.ListAPIView):
    queryset = Locador.objects.all()
    serializer_class = LocadorSerializers

class LocadorCriar(generics.CreateAPIView):
    queryset = Locador.objects.all()
    serializer_class = LocadorSerializers

class LocadorAtualizar(generics.UpdateAPIView):
    queryset = Locador.objects.all()
    serializer_class = LocadorSerializers
    lookup_field = 'id'

class LocadorDetalhar(generics.RetrieveAPIView):
    queryset = Locador.objects.all()
    serializer_class = LocadorSerializers
    lookup_field = 'id'

class LocadorApagar(generics.DestroyAPIView):
    queryset = Locador.objects.all()
    serializer_class = LocadorSerializers
    lookup_field = 'id'