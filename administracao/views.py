from django.shortcuts import render, redirect, get_object_or_404
from rolepermissions.decorators import has_permission_decorator
from . models import Users
from django.urls import reverse
from django.contrib import messages, auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def gerente(request):
    gerentes = Users.objects.filter(cargo='G')
    if request.method == 'GET':
        return render(request, 'gerente/gerente.html', {'gerentes': gerentes})

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

        user = Users.objects.filter(email=email)
        if user.exists():
            return HttpResponse('E-mail já existente')
        
        user = Users.objects.create_user(username=email,
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

@login_required(login_url='login', redirect_field_name='next')
def admin(request):
    return render(request, 'base.html')