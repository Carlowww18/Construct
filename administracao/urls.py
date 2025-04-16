from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    #GERENTE
    path('gerente/', views.gerente, name='gerente'),
    path('gerente_form/', views.gerente_form, name='gerente_form'),
    path('gerente_delete/<int:id>', views.gerente_delete, name='gerente_delete'),
    path('gerente_update/<int:id>', views.gerente_update, name='gerente_update'),

    #VENDEDOR
    path('vendedor/', views.vendedor, name='vendedor'),
    path('vendedor_form/', views.vendedor_form, name='vendedor_form'),
    path('vendedor_delete/<int:id>', views.vendedor_delete, name='vendedor_delete'),
    path('vendedor_update/<int:id>', views.vendedor_update, name='vendedor_update'),

    #CLIENTES
    path('cliente/', views.clientes, name='clientes'),
    path('cliente_form/', views.cliente_form, name='cliente_form'),
    path('cliente_delete/<int:id>', views.cliente_delete, name='cliente_delete'),
    path('cliente_update/<int:id>', views.cliente_update, name='cliente_update'),
]
