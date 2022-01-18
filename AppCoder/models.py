from django.db import models

# Create your models here.

class Usuario(models.Model):

    nombre=models.CharField(max_length=30)
    
    apellido=models.CharField(max_length=30)
    
    email=models.EmailField(max_length=50)

class Conductor(models.Model):

    nombre=models.CharField(max_length=30)
    
    apellido=models.CharField(max_length=30)
    
    email=models.EmailField()

    vehiculo=models.CharField(max_length=30)

    modelo=models.IntegerField()

    km=models.IntegerField()

class Soporte(models.Model):

    nombre=models.CharField(max_length=30)
    
    apellido=models.CharField(max_length=30)
    
    email=models.EmailField()



    
