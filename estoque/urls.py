from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.produtos, name='produtos'),
    path('vendas/', views.vendas, name='vendas'),
    path('vendas/venda_form/', views.venda_form, name='venda_form'),
    path('produtos_form/', views.produtos_form, name='produtos_form'),
    path('produtos_update/<int:id>', views.produtos_update, name='produtos_update'),
    path('produtos_delete/<int:id>', views.produtos_delete, name='produtos_delete')
]
