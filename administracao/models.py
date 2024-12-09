from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

class Users(AbstractUser):
    choice_cargo = (('V', 'Vendedor'),
                    ('G', 'Gerente'))
    cargo = models.CharField(max_length=1, choices=choice_cargo, blank=True)
    nome = models.CharField(max_length=150, blank=True)    
    sobrenome = models.CharField(max_length=150, blank=True)    
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF", blank=True)
    telefone = models.CharField(max_length=15, verbose_name="Telefone", blank=True)
    data_nascimento = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")
    endereco = models.CharField(max_length=80, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=50, blank=True)

    @property
    def idade(self):
        if self.data_nascimento:
            hoje = date.today()
            return hoje.year - self.data_nascimento.year - (
                (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day)
            )  