from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import *
# library aux
from validate_docbr import CPF, CNPJ
import re
# Create your views here.


def home(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        # verrificar se CPF e Senha informada é igual no BD
        user = authenticate(request, username=cpf, password=senha)
        if user is not None:
            login(request, user)
            return redirect('clientes-cadastro')
        else:
            messages.error(request, 'CPF ou Senha Incorreta!')
    return render(request, "home.html")


def logout_view(request):
    logout(request)
    return redirect('/')


def clientes_cadastro(request):
    if request.user.is_authenticated == True:
        nome = request.user.first_name
        sobre_nome = request.user.last_name
        # receber os dados de cadastro cliente
        save = False
        cpf_cnpj = request.POST.get('cpf_cnpj')  # validar CPF CNPJ
        # expressão regular para o codigo
        cpf_cnpj = re.sub('[^0-9]', '', cpf_cnpj)

        nome_cli = request.POST.get('nome')
        zap = request.POST.get('zap')
        # expressão regular para numero
        zap = re.sub('[^0-9]', '', zap)
        email = request.POST.get('email')
        endereco = request.POST.get('endereco')
        num = request.POST.get('num')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        complemento = request.POST.get('complemento')
        # validação do CPF ou CNPJ
        _cpf = CPF()
        _cnpj = CNPJ()
        if _cpf.validate(cpf_cnpj) == True:
            tipo_cliente = 'CPF'
        if _cnpj.validate(cpf_cnpj) == True:
            tipo_cliente = 'CNPJ'
        print(zap)
        context = {
            'nome': nome,
            'sobre_nome': sobre_nome
        }
        return render(request, "clientes-cadastro.html", context)
    else:
        return redirect('home')


def clientes_consulta(request):
    if request.user.is_authenticated == True:
        nome = request.user.first_name
        sobre_nome = request.user.last_name
        context = {
            'nome': nome,
            'sobre_nome': sobre_nome
        }
        return render(request, "clientes-consulta.html", context)
    else:
        return redirect('home')


def equipamentos_cadastro(request):
    if request.user.is_authenticated == True:
        nome = request.user.first_name
        sobre_nome = request.user.last_name
        context = {
            'nome': nome,
            'sobre_nome': sobre_nome
        }
        return render(request, "equipamentos.html", context)
    else:
        return redirect('home')
