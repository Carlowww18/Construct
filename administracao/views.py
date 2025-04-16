from django.shortcuts import render, redirect, get_object_or_404
from rolepermissions.decorators import has_permission_decorator
from . models import Users, Gerente, Vendedor, Clientes
from django.urls import reverse
from django.contrib import messages, auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# TELA INICIAL
@login_required(login_url='login', redirect_field_name='next')
def admin(request):
    return render(request, 'base.html')

# GERENTES
def gerente(request):
    gerentes = Gerente.objects.filter(cargo='G')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'gerente/gerente.html', {'gerentes': gerentes})
        else:
            return redirect(reverse('login'))

@has_permission_decorator('cadastrar_gerente')
def gerente_form(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'gerente/gerente_form.html')
        else:
            return redirect(reverse('login'))
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        endereco = request.POST.get('endereco')
        data_nascimento = request.POST.get('data_nascimento')
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('cpf')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')

        user = Gerente.objects.filter(email=email)
        if user.exists():
            return HttpResponse('E-mail já existente')
        
        user = Gerente.objects.create_user(username=email,  
                                           first_name=nome,
                                           last_name=sobrenome,
                                           email=email,                           
                                           password=senha, 
                                           endereco=endereco, 
                                           data_nascimento=data_nascimento,
                                           telefone=telefone,
                                           cpf=cpf,
                                           cidade=cidade,
                                           estado=estado,
                                           cargo='G')
        messages.add_message(request, messages.SUCCESS, 'Gerente cadastrado com sucesso')
        return render(request, 'gerente/gerente_form.html')

@has_permission_decorator('cadastrar_gerente')   
def gerente_delete(request, id):
    gerente = get_object_or_404(Users, id=id)
    gerente.delete()
    messages.add_message(request, messages.SUCCESS, 'Gerente excluído com sucesso')
    return redirect(reverse('gerente'))

@has_permission_decorator('cadastrar_gerente')
def gerente_update(request, id):
    gerentes = get_object_or_404(Users, id=id)
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'gerente/gerente_update.html', {'gerentes': gerentes})
        else:
            return redirect(reverse('login'))
    elif request.method == 'POST':
        gerentes.email = request.POST.get('email')
        gerentes.first_name = request.POST.get('nome')
        gerentes.last_name = request.POST.get('sobrenome')   
        gerentes.cpf = request.POST.get('cpf')
        gerentes.telefone = request.POST.get('telefone')
        gerentes.data_nascimento = request.POST.get('data_nascimento')
        gerentes.endereco = request.POST.get('endereco')
        gerentes.cidade = request.POST.get('cidade')
        gerentes.estado = request.POST.get('estado')
        gerentes.save()
        messages.add_message(request, messages.SUCCESS, f'Dados do gerente {gerentes.first_name} atualizados com sucesso')
        return redirect('gerente_update', id=id)  
    return render(request, 'gerente/gerente_update.html', {'gerentes': gerentes})

# LOGIN
def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('admin'))
        return render(request, 'login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=email, password=senha)

        if not user:
            return HttpResponse('Usuário inválido')
        
        auth.login(request, user)
        return redirect(reverse('admin'))
def logout(request):
    request.session.flush()
    return redirect(reverse('login'))


# VENDEDORES
def vendedor(request):
    vendedores = Vendedor.objects.filter(cargo='V')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'vendedor/vendedor.html', {'vendedores': vendedores})
        else:
            return redirect(reverse('login'))
        
@has_permission_decorator('cadastrar_vendedor')
def vendedor_form(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'vendedor/vendedor_form.html')
        else:
            return redirect(reverse('login'))
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        endereco = request.POST.get('endereco')
        data_nascimento = request.POST.get('data_nascimento')
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('cpf')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')

        user = Vendedor.objects.filter(email=email)
        if user.exists():
            return HttpResponse('E-mail já existente')
        
        user = Vendedor.objects.create_user(username=email,
                                            first_name=nome,
                                            last_name=sobrenome,
                                            email=email,                           
                                            password=senha, 
                                            endereco=endereco, 
                                            data_nascimento=data_nascimento,
                                            telefone=telefone,
                                            cpf=cpf,
                                            cidade=cidade,
                                            estado=estado,
                                            cargo='V')
        messages.add_message(request, messages.SUCCESS, 'Vendedor cadastrado com sucesso')
        return render(request, 'vendedor/vendedor_form.html')

def vendedor_delete(request, id):
    vendedor = get_object_or_404(Users, id=id)
    vendedor.delete()
    messages.add_message(request, messages.SUCCESS, 'Vendedor apagado com sucesso')
    return redirect(reverse('vendedor'))

@has_permission_decorator('cadastrar_vendedor')
def vendedor_update(request, id):
    vendedor = get_object_or_404(Users, id=id)
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'vendedor/vendedor_update.html', {'vendedor': vendedor})
        else:
            return redirect(reverse('login'))
    elif request.method == 'POST':
        vendedor.email = request.POST.get('email')
        vendedor.first_name = request.POST.get('nome')
        vendedor.last_name = request.POST.get('sobrenome')   
        vendedor.cpf = request.POST.get('cpf')
        vendedor.telefone = request.POST.get('telefone')
        vendedor.data_nascimento = request.POST.get('data_nascimento')
        vendedor.endereco = request.POST.get('endereco')
        vendedor.cidade = request.POST.get('cidade')
        vendedor.estado = request.POST.get('estado')
        vendedor.save()
        messages.add_message(request, messages.SUCCESS, f'Vendedor {vendedor.first_name} atualizado com sucesso')
        return redirect('vendedor_update', id=id)
    return render(request, 'vendedor/vendedor_update.html', {'vendedor': vendedor})

@has_permission_decorator('cadastrar_cliente')
def clientes(request):
    cliente = Clientes.objects.all()
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'cliente/cliente.html', {'cliente': cliente})
        else:
            return redirect(reverse('login'))
        
@has_permission_decorator('cadastrar_cliente')
def cliente_form(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'cliente/cliente_form.html')
        else:
            return redirect(reverse('login'))
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        data_nascimento = request.POST.get('data_nascimento')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        email = request.POST.get('email')

        user = Clientes.objects.filter(email=email)
        if user.exists():
            messages.add_message(request, messages.ERROR, 'E-mail já existente')
        
        user = Clientes.objects.create(nome=nome,
                                       sobrenome=sobrenome,
                                       data_nascimento=data_nascimento,
                                       cpf=cpf,
                                       telefone=telefone,
                                       endereco=endereco,
                                       email=email)
        messages.add_message(request, messages.SUCCESS, 'Cliente cadastrado com sucesso')
        return render(request, 'cliente/cliente_form.html')

@has_permission_decorator('cadastrar_cliente')
def cliente_delete(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    cliente.delete()
    messages.add_message(request, messages.SUCCESS, 'Cliente deletado com sucesso!')
    return redirect(reverse('clientes'))

@has_permission_decorator('cadastrar_cliente')
def cliente_update(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'cliente/cliente_update.html', {'clientes': cliente})
        else:
            return redirect(reverse('login'))
    elif request.method == 'POST':
        cliente.email = request.POST.get('email')
        cliente.nome = request.POST.get('nome')
        cliente.sobrenome = request.POST.get('sobrenome')   
        cliente.cpf = request.POST.get('cpf')
        cliente.telefone = request.POST.get('telefone')
        cliente.data_nascimento = request.POST.get('data_nascimento')
        cliente.endereco = request.POST.get('endereco')
        cliente.save()
        messages.add_message(request, messages.SUCCESS, 'Cliente atualizado com sucesso')
        return redirect('cliente_update', id=id)
    return render(request, 'cliente/cliente_update.html', {'clientes': cliente})