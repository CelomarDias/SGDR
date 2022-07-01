
from django.db import models

class SGDR(models.Model):

    tipo = models.CharField(max_length=50)

    peso = models.CharField(max_length=20)

    quantidade = models.CharField(max_length=30)

    data_criacao = models.DateField(default=None, null=True)


# Create your models here.
