from fileinput import filename
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import *
from django.core.files.storage import FileSystemStorage
# library aux
from validate_docbr import CPF, CNPJ
import re
from lladmin.models import cliente, equipamento
import os


def home(request):
    if request.method == 'POST':
        cpf = str(request.POST.get('cpf'))
        cpf = re.sub('[^0-9]', '', cpf)
        senha = request.POST.get('senha')
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
        save = False
        cpf_cnpj = str(request.POST.get('cpf_cnpj'))
        cpf_cnpj = re.sub('[^0-9]', '', cpf_cnpj)
        nome_cli = request.POST.get('nome')
        zap = str(request.POST.get('zap'))
        zap = re.sub('[^0-9]', '', zap)
        email = request.POST.get('email')
        endereco = request.POST.get('endereco')
        num = request.POST.get('num')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        complemento = request.POST.get('complemento')

        _cpf = CPF()
        _cnpj = CNPJ()
        if _cpf.validate(cpf_cnpj) == True:
            save = True
            tipo_cliente = 'CPF'
        elif _cnpj.validate(cpf_cnpj) == True:
            save = True
            tipo_cliente = 'CNPJ'

        if request.method == 'POST':
            if cpf_cnpj in str(cliente.objects.values_list('cpf_cnpj')):
                messages.error(request, 'CPF ou CNPJ já está cadastrado!')
                #save = False
            # salvar os anexos
            pasta = ('anexos/'+cpf_cnpj)
            for i in range(1, 21):
                file = request.FILES.get('f'+str(i))
                if file != None:
                    fs = FileSystemStorage(location=pasta)
                    fs.save(file.name, file)

            if save == True:
                novo_cliente = cliente(cpf_cnpj=cpf_cnpj, tipo_cliente=tipo_cliente, nome_completo=nome_cli, whatsapp=zap,
                                       email=email, endereco=endereco, numero=num, cidade=cidade, bairro=bairro, estado=estado, complemento=complemento)
                novo_cliente.save()
                messages.success(request, 'Cliente cadastrado com suceesso!')

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
        clientes = cliente.objects.values_list(
            'cpf_cnpj', 'tipo_cliente', 'nome_completo', 'whatsapp', 'email', 'endereco', 'numero', 'bairro', 'cidade', 'estado',  'complemento', 'cep', named=True)
        cpfs = clientes.filter(tipo_cliente='CPF')
        cnpjs = clientes.filter(tipo_cliente='CNPJ')
        tot_cpfs, tot_cnpjs = len(cpfs), len(cnpjs)
        pessoas = {}
        empresas = {}
        for i in cpfs:
            pessoas[i[2]] = i[3]
        for i in cnpjs:
            empresas[i[2]] = i[3]
        consulta = False
        consulta_cliente = ''
        if request.method == 'POST':
            consulta_cliente = request.POST.get('consulta_cliente')
            if len(consulta_cliente) > 0:
                consulta_cliente = clientes.filter(
                    nome_completo__contains=consulta_cliente)
                consulta = True
        context = {
            'consulta_cliente': consulta_cliente,
            'nome': nome,
            'sobre_nome': sobre_nome,
            'pessoas': pessoas,
            'empresas': empresas,
            'tot_cpfs': tot_cpfs,
            'tot_cnpjs': tot_cnpjs,
            'consulta': consulta,
        }
        return render(request, "clientes-consulta.html", context)
    else:
        return redirect('home')


def equipamentos(request):
    if request.user.is_authenticated == True:
        nome = request.user.first_name
        sobre_nome = request.user.last_name
        equipamentos = equipamento.objects.values_list(
            'tipo', 'descricao', 'fabricante', 'modelo', 'potencia', named=True)
        context = {
            'nome': nome,
            'sobre_nome': sobre_nome,
            'equipamentos': equipamentos
        }
        if request.method == 'POST':
            tipo = request.POST.get('tipo')
            descricao = request.POST.get('descricao')
            fabricante = request.POST.get('fabricante')
            modelo = request.POST.get('modelo')
            potencia = request.POST.get('potencia')
            if potencia == '':
                potencia = 0
            if fabricante == '':
                fabricante = '-'
            if modelo == '':
                modelo = '-'
            novo_eq = equipamento(tipo=tipo, descricao=descricao,
                                  fabricante=fabricante, modelo=modelo, potencia=potencia)
            novo_eq.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
        return render(request, "equipamentos.html", context)
    else:
        return redirect('home')
