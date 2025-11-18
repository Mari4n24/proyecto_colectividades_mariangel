from django.db import models

class Colectividad(models.Model):
    nombre = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    
    def __str__(self):
        return f'Colectividad ({self.id}) : {self.nombre} - {self.pais}'
