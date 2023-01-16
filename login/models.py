from django.db import models
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models


class Cadastrar(models.Model):
    usuario2 = models.CharField(max_length=15)
    email = models.CharField(max_length=40, null=False, blank=False, default="email@technobox.com")
    senha2 = models.CharField(max_length=20)
    confirmasenha = models.CharField(max_length=20)