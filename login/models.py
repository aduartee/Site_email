from django.db import models
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

class Login(models.Model):
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
