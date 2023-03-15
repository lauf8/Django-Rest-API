from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Objetos

@receiver(signals.pre_save, sender=Objetos)

def generate_codigo(sender, instance, created, **kwargs):
    if not instance.codigo:

        instance.codigo = 23

post_save.connect(generate_codigo, Objetos)