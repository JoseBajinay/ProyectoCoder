from django.db import models
from datetime import datetime

# Create your models here.
class Pariente (models.Model):
    nombre = models.CharField(max_length=30)
    parentesco = models.CharField(max_length=15)
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()
    
    