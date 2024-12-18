from django.contrib import admin
from . models import Users
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