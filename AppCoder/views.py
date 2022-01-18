
from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Soporte, Usuario, Conductor

# Create your views here.

def usuario(self):

    prueba= Usuario(nombre="nicolas", apellido="Montiel", email="nicom2852000gmailcom")
    prueba.save()
    documento=f"nombre={prueba.nombre} apellido= {prueba.apellido} mail= {prueba.email}"
    return HttpResponse(documento)

def soporte(self):

    sop= Soporte(nombre="leonel", apellido="messi", email="leo@gmailcom")
    sop.save()
    documentoo=f"hola {sop.nombre}"
    return HttpResponse(documentoo)

def conductor(self):

    cond= Conductor(nombre="tito", apellido="perez", email="titoperezgmailcom",  vehiculo="fiat uno", modelo= 2013 , km= 100000)
    cond.save()
    docu=f"{cond.nombre} {cond.apellido} {cond.email} {cond.vehiculo} {cond.km} {cond.modelo}"
    return HttpResponse(docu)
    
