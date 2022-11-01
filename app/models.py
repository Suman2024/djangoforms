from socket import fromshare
from unittest.util import _MAX_LENGTH
from django.db import models
# Create your models here.
class Topic(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField()
