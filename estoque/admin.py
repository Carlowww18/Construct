from django.contrib import admin
from .models import Categoria, Produtos, Venda, ItemVenda

admin.site.register(Categoria)
admin.site.register(Produtos)
admin.site.register(Venda)
admin.site.register(ItemVenda)