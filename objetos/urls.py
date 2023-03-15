from objetos.views import ObjetosCriar, ObjetosListar, ObjetosDetalhar,ObjetosDetalhar, ObjetosApagar
from django.urls import path 

urlpatterns = [
    path('', ObjetosListar.as_view(), name='listar_objeto'),
    path('create', ObjetosCriar.as_view(), name='criar_objeto'),
    path('update/<int:id>', ObjetosDetalhar.as_view(), name='atualizar_objeto'),
    path('delete/<int:id>', ObjetosApagar.as_view(), name='apagar_objeto'),
    path('<int:id>', ObjetosDetalhar.as_view(), name='detalhar_objeto'),
 ]
 