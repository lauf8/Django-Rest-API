# Generated by Django 4.1.7 on 2023-03-13 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objetos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('codigo', models.CharField(max_length=32)),
                ('estado', models.CharField(choices=[('Novo', 'Novo'), ('Semi-novo', 'Semi-novo'), ('Usado', 'Usado')], default='Novo', max_length=30)),
                ('tipo', models.CharField(choices=[('Drone', 'Drone'), ('Microcontrolador', 'Microcontrolador'), ('Processador', 'Processador'), ('Placa Mãe', 'Placa Mãe'), ('MicroChip', 'MicroChip'), ('Outros', 'Outros')], default='Drone', max_length=30)),
                ('observacao', models.TextField()),
                ('status', models.CharField(choices=[('Disponível', 'Disponível'), ('Emprestado', 'Emprestado'), ('Indisponível', 'Indisponível')], default='Disponível', max_length=15)),
                ('motivo_indisponivel', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
