from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('login', views.login, name='login'),
    path('logotu', views.logout, name='logout')
]
