# Generated by Django 3.2.7 on 2021-09-06 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_cliente_sexo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='endereço',
            new_name='endereco',
        ),
    ]
