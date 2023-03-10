from django.db import models
from cpf_field.models import CPFField
from helpers.models import TrackingModel

class Locador(TrackingModel):
    nome = models.CharField(max_length=100,null=False)
    matricula = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200, null=False)
    curso = models.CharField(max_length=50)
    email = models.EmailField(max_length=150, null=False)
    telefone = models.CharField(max_length=20, null=False)
    cpf = CPFField('cpf')
    STATUS_CHOICES = (
        ('Elegível', 'Elegível'),
        ('Suspenso', 'Suspenso'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Elegível')
    motivo_suspensao = models.TextField()
    def __str__(self):
        return self.nome
    
    pass


