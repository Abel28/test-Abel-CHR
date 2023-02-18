from django.db import models

# Create your models here.

class Project(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    tipologia = models.CharField(max_length=255)
    titular = models.CharField(max_length=255)
    inversion = models.CharField(max_length=255)
    fecha = models.CharField(max_length=255)
    estado = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombre
    
