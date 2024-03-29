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
    email3 = models.EmailField(max_length=62)
    demanda3 = models.CharField(max_length=5)
    nprovedor2 =  models.CharField(max_length= 52)
    
    
    def __str__(self) -> str:
        return self.nome
    
class Origindown(models.Model):
    origin4 = models.CharField(max_length=30)
    email4 = models.EmailField(max_length=30)
    ndemanda4 = models.CharField(max_length=30)
    nprovedor4 = models.CharField(max_length=30, default='PROVEDOR')
    
    def __str__(self) -> str:
        return self.email4
    
    
class Downedge(models.Model):
    edge5 = models.CharField(max_length=30)
    email5 = models.EmailField(max_length=30)
    ndemanda5 = models.CharField(max_length=30)
    nprovedor5 = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.email5
    
    
class Downvod(models.Model):
    vod = models.CharField(max_length=30)
    email6 = models.EmailField(max_length=30)
    ndemanda6 = models.CharField(max_length=30)
    nprovedor6 = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.email6
    
    
class Downoriginvod(models.Model):
    origin8 = models.CharField(max_length=30, default='Origin')
    vod1 = models.CharField(max_length=30)
    email7 = models.EmailField(max_length=30)
    ndemanda7 = models.CharField(max_length=30)
    nprovedor7 = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.email7
    
    
class Downedgevod(models.Model):
    edge8 = models.CharField(max_length=30)
    vod2 = models.CharField(max_length=30)
    email8 = models.EmailField(max_length=30)
    ndemanda8 = models.CharField(max_length=30)
    nprovedor8 = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.email8
    

class Downoriginedgevod(models.Model):
    origin7 = models.CharField(max_length=30)
    edge9 = models.CharField(max_length=30)
    vod3 = models.CharField(max_length=30)
    email9 = models.EmailField(max_length=30)
    ndemanda9 = models.CharField(max_length=30)
    nprovedor9 = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.email9