from django.db import models

# Create your models here.

class Asesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    id_asesor = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Evaluador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    id_evaluador = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Evaluacion(models.Model):
    id_evaluador = models.CharField(max_length=30)
    id_asesor = models.CharField(max_length=30)
    id_evaluacion = models.CharField(max_length=30)
    fecha_evaluacion = models.DateField()
    
    def __str__(self):
        return f'Codigo de evaluacion: {self.id_evaluacion}'