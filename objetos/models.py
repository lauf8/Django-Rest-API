from django.db import models
from helpers.models import TrackingModel
from helpers.random import gerar_caracteres_aleatorios
from django.dispatch import receiver 
from django.db.models.signals import pre_save
from django.dispatch import receiver



class Objetos(TrackingModel):
    codigo = models.CharField(max_length=32)
    ESTADO_CHOICES = (
        ('Novo', 'Novo'),
        ('Semi-novo', 'Semi-novo'),
        ('Usado', 'Usado'),
    )
    estado = models.CharField(max_length=30, choices=ESTADO_CHOICES, default='Novo')
    TIPO_CHOICES = (
        ('Drone', 'Drone'),
        ('Microcontrolador', 'Microcontrolador'),
        ('Processador', 'Processador'),
        ('Placa Mãe', 'Placa Mãe'),
        ('MicroChip', 'MicroChip'),
        ('Outros', 'Outros'),

    )

    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES, default='Drone')
    observacao = models.TextField()
    status = STATUS_CHOICES = (
        ('Disponível', 'Disponível'),
        ('Emprestado', 'Emprestado'),
        ('Indisponível', 'Indisponível'),
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Disponível')
    motivo_indisponivel = models.TextField()

@receiver(pre_save, sender=Objetos)
def check_product_description(sender, instance, **kwargs):
    if not instance.codigo:
        valor = gerar_caracteres_aleatorios(10)
        if  instance.tipo == "Drone":
            valor = "DR" + valor  

        elif instance.tipo == "Microcontrolador":
            valor = "MC" + valor  

        elif instance.tipo == "Processador":
            valor = "PR" + valor  

        elif instance.tipo == "Placa Mãe":
            valor = "PM" + valor  

        elif instance.tipo == "MicroChip":
            valor = "CH" + valor  

        elif instance.tipo == "Outros":
            valor = "OU" + valor  
        
        instance.codigo = valor




        
    
# Create your models here.
