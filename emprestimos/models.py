from helpers.models import TrackingModel
from django.db import models
from objetos.models import Objetos
from app.models import Locador

class Emprestimo(TrackingModel):
    objeto_emprestimo = models.ManyToManyField("objetos.Objetos", related_name ="objetos")
    locador = models.ForeignKey(Locador, on_delete=models.CASCADE)
    data_devolucao = models.DateField()
    status = models.BooleanField()
