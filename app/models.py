""" https://docs.djangoproject.com/en/4.2/ref/models/fields/ """

from django.db import models

# Create your models here.
class Processos(models.Model):
    Protocolo = models.IntegerField(max_length=10)
    Status = models.CharField(max_length=30)
    Paciente = models.CharField(max_length=30)
    Materiais_Identificado = models.CharField(max_length=30)
    Informe_de_Uso = models.CharField(max_length=3)
    Nota_Fiscal = models.IntegerField(max_length=10)
    Setor = models.CharField(max_length=20)
    Processo = models.CharField(max_length=30)
    
 