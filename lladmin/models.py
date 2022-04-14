from django.db import models


class cliente(models.Model):
    cpf_cnpj = models.CharField(primary_key=True, max_length=14)
    tipo_cliente = models.CharField(max_length=4)  # CPF ou CNPJ
    nome_completo = models.CharField(max_length=150)
    whatsapp = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    cep = models.CharField(max_length=8, default=0)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    complemento = models.CharField(max_length=500)

    def __str__(self):
        return self.cpf_cnpj


class equipamento(models.Model):
    tipo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=150)
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    potencia = models.IntegerField()

    def __str__(self):
        return self.descricao
