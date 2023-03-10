from django.urls import path 
from autenticacao.views import Register

urlpatterns = [
    path('register', Register.as_view(), name='registrar'),
]
 