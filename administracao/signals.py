from django.dispatch import receiver
from django.db.models.signals import post_save
from . models import Users, Gerente, Vendedor
from rolepermissions.roles import assign_role

@receiver(post_save, sender=Users)
def define_permissioes(sender, instance, created, **kwargs):
    if created:
        if instance.cargo == 'V':
            assign_role(instance, 'vendedor')
        elif instance.cargo == 'G':
            assign_role(instance, 'gerente')

@receiver(post_save, sender=Gerente)
def define_permissioes(sender, instance, created, **kwargs):
    if created:
        if instance.cargo == 'G':
            assign_role(instance, 'gerente')

@receiver(post_save, sender=Vendedor)
def vendedor_permissioes(sender, instance, created, **kwargs):
    if created:
        if instance.cargo == 'V':
            assign_role(instance, 'vendedor')