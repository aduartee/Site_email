from unittest.util import _MAX_LENGTH
from django.db import models

class Cdntv(models.Model):
    origin = models.CharField(max_length=26)
    senha = models.CharField(max_length=25)
    edge = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    titulo = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.origin