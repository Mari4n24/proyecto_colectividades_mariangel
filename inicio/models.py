from django.db import models

class Colectividad(models.Model):
    nombre = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
