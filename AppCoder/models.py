from django.db import models

# Create your models here.
class Inicio(models.Model):

    principal=models.CharField(max_length=30)
    
class Usuario(models.Model):

    nombre=models.CharField(max_length=30)

    #contraseña=models.CharField(max_length=20)    
    
    apellido=models.CharField(max_length=30)
    
    email=models.EmailField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Conductor(models.Model):

    nombre=models.CharField(max_length=30)

    #contraseña=models.CharField(max_length=20) 
    
    apellido=models.CharField(max_length=30)
    
    email=models.EmailField()

    vehiculo=models.CharField(max_length=30)

    modelo=models.IntegerField()

    km=models.IntegerField()

class Soporte(models.Model):

    nombre=models.CharField(max_length=30)

    #contraseña=models.CharField(max_length=20) 
    
    apellido=models.CharField(max_length=30)
    
    email=models.EmailField()



    
#ubertrucho
#12345