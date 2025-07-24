from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("area/", include('administracao.urls')),
    path("estoque/", include('estoque.urls')),
    path("authentication/", include('authentication.urls')),
]
