from app.views import LocadorCriar, LocadorListar, LocadorAtualizar, LocadorApagar, LocadorDetalhar
from django.urls import path 

urlpatterns = [
    path('', LocadorListar.as_view(), name='listar_locador'),
    path('create', LocadorCriar.as_view(), name='criar_locador'),
    path('update/<int:id>', LocadorAtualizar.as_view(), name='atualizar_locador'),
    path('delete/<int:id>', LocadorApagar.as_view(), name='apagar_locador'),
    path('<int:id>', LocadorDetalhar.as_view(), name='detalhar_locador'),
 ]
 