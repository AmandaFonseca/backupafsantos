# Generated by Django 3.2.7 on 2021-09-07 00:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_cliente_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='salario',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=18, validators=[django.core.validators.RegexValidator(message="O número de telefone deve ser inserido no formato: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
