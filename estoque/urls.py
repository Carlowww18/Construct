from django.urls import path, include
from . import views
from . views import ProdutoViewSet, VendaViewSet, ItemVendaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('produtos', ProdutoViewSet)
router.register('vendas', VendaViewSet)
router.register('item', ItemVendaViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),

    path('produtos/', views.produtos, name='produtos'),
    path('vendas/', views.vendas, name='vendas'),
    path('vendas/venda_form/', views.venda_form, name='venda_form'),
    path('listar_vendas/', views.listar_vendas, name='listar_vendas'),
    path('detalhe_venda/<int:id>', views.detalhe_venda, name='detalhe_venda'),
    path('cancelar_venda/<int:id>', views.cancelar_venda, name='cancelar_venda'),
    path('produtos_form/', views.produtos_form, name='produtos_form'),
    path('produtos_update/<int:id>', views.produtos_update, name='produtos_update'),
    path('produtos_delete/<int:id>', views.produtos_delete, name='produtos_delete')
]
