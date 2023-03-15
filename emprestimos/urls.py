from emprestimos.views import *
from django.urls import path 

urlpatterns = [
    path('', EmprestimoListar.as_view(), name='listar_objeto'),
    path('create', EmprestimoCriar.as_view(), name='criar_objeto'),
    path('update/<int:id>', EmprestimoDetalhar.as_view(), name='atualizar_objeto'),
    path('delete/<int:id>', EmprestimoApagar.as_view(), name='apagar_objeto'),
    path('<int:id>', EmprestimoDetalhar.as_view(), name='detalhar_objeto'),
 ]
 