from django.db import models


class cliente(models.Model):
    cpf_cnpj = models.CharField(primary_key=True, max_length=14)
    tipo_cliente = models.CharField(max_length=4)  # CPF ou CNPJ
    nome_completo = models.CharField(max_length=150)
    whatsapp = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    cep = models.CharField(max_length=12, default=0)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    complemento = models.CharField(max_length=500)
    anexos = models.CharField(max_length=950)

    def __str__(self):
        return self.cpf_cnpj


class contrato(models.Model):
    # chave estrangeira do cnpj_cpf_cliente
    cpf_cnpj_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    conta_contrato = models.CharField(primary_key=True, max_length=20)
    cpf_cnpj_contrato = models.CharField(
        max_length=14, default=None)
    consumo = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.conta_contrato


class conta(models.Model):
    # chave estrangeira contra_contrato
    conta = models.ForeignKey(contrato, on_delete=models.CASCADE)
    data_ref = models.DateField(default=None)
    consumo = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.conta)


class equipamento(models.Model):
    tipo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=150)
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    potencia = models.IntegerField()

    def __str__(self):
        return self.descricao
