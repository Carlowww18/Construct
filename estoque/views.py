from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from . models import Produtos, Categoria, Venda, ItemVenda
from administracao.models import Clientes
from django.contrib import messages
from rolepermissions.decorators import has_permission_decorator

def produtos(request):
    produtos = Produtos.objects.all()
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'produtos/produtos.html', {'produtos': produtos,})
        return redirect(reverse('login'))

@has_permission_decorator('cadastrar_produtos') 
def produtos_form(request):
    categoria = Categoria.objects.all()
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'produtos/produtos_form.html', {'categoria': categoria})
        return redirect(reverse('login'))
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        quantidade = request.POST.get('quantidade')
        categoria = request.POST.get('categoria')
        preco_compra = request.POST.get('preco_compra')
        preco_venda = request.POST.get('preco_venda')

        produto = Produtos(nome=nome, quantidade=quantidade, categoria_id=categoria, preco_compra=preco_compra, preco_venda=preco_venda)
        produto.save()
        messages.add_message(request, messages.SUCCESS, 'Produto cadastrado com sucesso')

        return redirect(reverse('produtos_form'))

@has_permission_decorator('cadastrar_produtos')   
def produtos_update(request, id):
    produtos = get_object_or_404(Produtos, id=id)
    quantidade_format = str(produtos.quantidade).replace(',', '.')
    preco_compra_format = str(produtos.preco_compra).replace(',', '.')
    preco_venda_format = str(produtos.preco_venda).replace(',', '.')
    categoria = Categoria.objects.all()
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'produtos/produtos_update.html', {'produtos':produtos,
                                                                     'categoria': categoria,
                                                                     'quantidade': quantidade_format,
                                                                     'preco_compra': preco_compra_format,
                                                                     'preco_venda': preco_venda_format})
        return redirect(reverse('login'))
    elif request.method == 'POST':
        produtos.nome = request.POST.get('nome')
        produtos.quantidade = request.POST.get('quantidade')
        categoria_id = request.POST.get('categoria')
        produtos.preco_compra = request.POST.get('preco_compra')
        produtos.preco_venda = request.POST.get('preco_venda')

        if categoria_id:
            produtos.categoria = get_object_or_404(Categoria, id=categoria_id)

        produtos.save()
        messages.add_message(request, messages.SUCCESS, 'Produto atualizado com sucesso')
        return redirect('produtos_update', id=id)
    
@has_permission_decorator('cadastrar_produtos')    
def produtos_delete(request, id):
    produtos = get_object_or_404(Produtos, id=id)
    produtos.delete()
    messages.add_message(request, messages.SUCCESS, 'Produto deletado com sucesso')
    return redirect('produtos')
    
@has_permission_decorator('realizar_venda')
def vendas(request):
    produtos = Produtos.objects.all().values('id', 'nome', 'preco_venda')
    clientes = Clientes.objects.all()
    return render(request, 'vendas/vendas.html', {'produtos': list(produtos),
                                                  'clientes': clientes,
                                                  'now': timezone.now()})

@has_permission_decorator('realizar_venda')
def venda_form(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'vendas/vendas.html')
        return redirect(reverse('login'))
    if request.method == 'POST':
        cliente = request.POST.get('cliente_id')

        venda = Venda.objects.create(cliente_id=cliente, vendedor=request.user.vendedor)

        contador = 0
        while True:
            produto = request.POST.get(f'produto_{contador}')
            quantidade = request.POST.get(f'quantidade_{contador}')
            preco = request.POST.get(f'preco_{contador}')

            if not produto:
                break

            ItemVenda.objects.create(
                venda=venda,
                produto_id=produto,
                quantidade=float(quantidade),
                preco_unitario=preco
            )
            contador+=1


        total = sum(item.quantidade * item.preco_unitario for item in venda.itens.all())
        venda.total = total
        venda.save()
        messages.add_message(request, messages.SUCCESS, 'Venda realizada com sucesso')

        return redirect('vendas')

@has_permission_decorator('realizar_venda')    
def listar_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'vendas/listar_vendas.html', {'vendas': vendas})

@has_permission_decorator('realizar_venda')  
def detalhe_venda(request, id):
    venda = get_object_or_404(Venda, id=id)
    return render(request, 'vendas/detalhe_venda.html', {'venda': venda})

@has_permission_decorator('realizar_venda')  
def cancelar_venda(request, id):
    venda = get_object_or_404(Venda, id=id)
    venda.cancelada = True
    venda.save()
    messages.add_message(request, messages.SUCCESS, f'Venda N° {venda.id} cancelada com sucesso')

    if venda.cancelada:
        for item in venda.itens.all():
            item.produto.quantidade += item.quantidade
            item.produto.save()

    return redirect('listar_vendas') 