# Generated by Django 4.0.1 on 2022-04-14 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lladmin', '0002_alter_cliente_whatsapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cep',
            field=models.CharField(default=0, max_length=8),
        ),
    ]
