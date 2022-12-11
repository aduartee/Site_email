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
    
    
class VOD(models.Model):
    origin2 = models.CharField(max_length=70)
    edge2 = models.CharField(max_length=45)
    email2= models.CharField(max_length=60)
    demanda2 = models.CharField(max_length=5)
    nprovedor = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.origin2
    

class Aplicativos(models.Model):
    nome = models.CharField(max_length=40)
    mobile = models.CharField(max_length=43)
    stb = models.CharField(max_length=50)
    ios = models.CharField(max_length=50)
    apks = models.CharField(max_length=60)
    self_email = models.CharField(max_length=40, default='EMAIL')
    email3 = models.CharField(max_length=62)
    demanda3 = models.CharField(max_length=5)
    nprovedor2 =  models.CharField(max_length= 52)
    
    
    def __str__(self) -> str:
        return self.nome
    
    
