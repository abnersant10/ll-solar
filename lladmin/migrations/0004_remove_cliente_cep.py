# Generated by Django 4.0.1 on 2022-04-16 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lladmin', '0003_cliente_cep'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cep',
        ),
    ]
