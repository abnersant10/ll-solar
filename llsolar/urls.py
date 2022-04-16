"""llsolar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lladmin.views import home, clientes_cadastro, clientes_consulta, equipamentos, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # aqui seria a página inicial
    path('clientes/cadastro', clientes_cadastro, name='clientes-cadastro'),
    path('clientes/consulta', clientes_consulta, name='clientes-consulta'),
    path('equipamentos', equipamentos,
         name='equipamentos'),
    path('logout', logout_view, name="logout"),
]
