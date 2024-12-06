from django.shortcuts import render, redirect
from rolepermissions.decorators import has_permission_decorator
from . models import Users
from django.urls import reverse
from django.contrib import messages, auth
from django.http import HttpResponse


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('admin'))
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=username, password=senha)

        if not user:
            return HttpResponse('Usuário inválido')
        
        auth.login(request, user)
        return redirect(reverse('admin'))
def logout(request):
    request.session.flush()
    return redirect(reverse('login'))

def admin(request):
    return render(request, 'base.html')