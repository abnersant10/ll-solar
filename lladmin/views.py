from urllib import request
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html")


def clientes_cadastro(request):
    pass


def clientes_consulta(request):
    pass


def equipamentos_cadastro(request):
    pass
