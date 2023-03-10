from rest_framework import generics
from autenticacao.serialzers import UserSerializers
from autenticacao.models import User

class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_field = 'id'
