from urllib import request
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import *
# Create your views here.


def home(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        # verrificar se CPF e Senha informada é igual no BD
        user = authenticate(request, username=cpf, password=senha)
        if user is not None:
            login(request, user)
            return redirect('clientes_cadastro')
        else:
            messages.error(request, 'CPF ou Senha Incorreta!')
    return render(request, "home.html")


def logout_view(request):
    logout(request)
    return redirect('/')


def clientes_cadastro(request):
    if request.user.is_authenticated == True:
        return render(request, "clientes_cadastro.html")


def clientes_consulta(request):
    pass


def equipamentos_cadastro(request):
    pass
