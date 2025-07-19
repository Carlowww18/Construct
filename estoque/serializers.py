from rest_framework import serializers 
from . models import Produtos, Venda, ItemVenda


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'