from django.db import models
from django.template.defaultfilters import slugify
from administracao.models import Clientes, Users, Vendedor


class Categoria(models.Model):
    titulo = models.CharField(max_length=40)

    def __str__(self):
        return self.titulo

class Produtos(models.Model):
    nome = models.CharField(max_length=40, unique=True, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    quantidade = models.FloatField(default=0)
    preco_compra = models.FloatField()
    preco_venda = models.FloatField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        return super().save(*args, **kwargs)
    
    def gerar_desconto(self, desconto):
        return self.preco_compra - (self.preco_venda * (desconto /100)) 
    
    def lucro(self):
        lucro = self.preco_venda - self.preco_compra
        return (lucro * 100) / self.preco_compra
    
class Imagem(models.Model):
    imagem = models.ImageField(upload_to="imagem_produto")
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)

class Venda(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.SET_NULL, null=True, blank=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0)
    cancelada = models.BooleanField(default=False)

    def __str__(self):
        return f'venda: {self.id} -- {self.data.strftime('%d/%m/%Y')}'
    
class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produtos, on_delete=models.PROTECT)
    quantidade = models.FloatField()
    preco_unitario = models.FloatField()

    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f'{self.venda} -- {self.produto}'
