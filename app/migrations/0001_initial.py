# Generated by Django 4.2 on 2023-07-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Processos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Protocolo', models.IntegerField(max_length=10)),
                ('Status', models.CharField(max_length=30)),
                ('Paciente', models.CharField(max_length=30)),
                ('Materiais_Identificado', models.CharField(max_length=30)),
                ('Informe_de_Uso', models.CharField(max_length=3)),
                ('Nota_Fiscal', models.IntegerField(max_length=10)),
                ('Setor', models.CharField(max_length=20)),
                ('Processo', models.CharField(max_length=30)),
            ],
        ),
    ]