from django.contrib import admin
from . models import Users, Gerente, Vendedor, Clientes
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth import admin as admin_auth_django


@admin.register(Users)
class UserAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Cargo', {'fields': ('cargo',)}),
    )

@admin.register(Gerente)
class GerenteAdmin(UserAdmin):
    model = Gerente
    fieldsets = UserAdmin.fieldsets 

@admin.register(Vendedor)
class VendedorAdmin(UserAdmin):
    model = Vendedor
    fieldsets = UserAdmin.fieldsets

admin.site.register(Clientes)