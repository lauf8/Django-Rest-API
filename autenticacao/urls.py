from django.urls import path 
from autenticacao.views import Register, UserList, UserList

urlpatterns = [
    path('register', Register.as_view(), name='registrar'),
    path('list', UserList.as_view(), name='registrar'),
    path('<int:id>', UserList.as_view(), name='registrar'),
]
 