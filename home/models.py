from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

class Cdntv(models.Model):
    origin = models.CharField(max_length=26)
    senha = models.CharField(max_length=25)
    edge = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    titulo = models.CharField(max_length=50)
    demanda = models.CharField(max_length=5, default='VALOR')
    provedor = models.CharField(max_length=50, default='VALOR')
    
    def __str__(self) -> str:
        return self.origin