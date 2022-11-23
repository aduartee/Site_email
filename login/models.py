from django.db import models
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models


class Cadastrar(models.Model):
    usuario2 = models.CharField(max_length=50)
    senha2 = models.CharField(max_length=50)
    confirmasenha = models.CharField(max_length=50)