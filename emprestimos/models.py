from helpers.models import TrackingModel
from django.db import models
from objetos.models import Objetos
from app.models import Locador
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

class Emprestimo(TrackingModel):
    objeto_emprestimo = models.ManyToManyField("objetos.Objetos", related_name ="objetos")
    locador = models.ForeignKey(Locador, on_delete=models.CASCADE)
    data_devolucao = models.DateField()
    status = models.BooleanField()

    def __str__(self):
        return self.locador + self.objeto_emprestimo


    def atualizar_status_objeto_emprestado(self):
        emprestados = set(self.objeto_emprestimo.all())
        for obj in Objetos.objects.filter(status="Disponível"):
            if obj not in emprestados:
                obj.status = 'Disponível'
                obj.save()
        for obj in emprestados:
            obj.status = 'Emprestado'
            obj.save()

@receiver(m2m_changed, sender=Emprestimo.objeto_emprestimo.through)
def emprestimo_objetos_changed(sender, instance, **kwargs):
    instance.atualizar_status_objeto_emprestado()