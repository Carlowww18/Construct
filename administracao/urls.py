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
]
