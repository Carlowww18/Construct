from django.dispatch import receiver
from django.db.models.signals import post_save
from . models import Produtos, ItemVenda, Venda

@receiver(post_save, sender=ItemVenda)
def atualizar_estoque_apos_venda(sender, created, instance, **kwargs):
    if created:
        produto = instance.produto
        produto.quantidade -= instance.quantidade
        produto.save()