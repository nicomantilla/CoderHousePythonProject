from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Soporte, Usuario, Conductor


#def usuario(self):
#    user= Usuario(nombre="nicolas", apellido="Montiel", email="nicom2852000gmailcom")
#    user.save()
#    documento=f"nombre={user.nombre} apellido= {user.apellido} mail= {user.email}"
#    return HttpResponse(documento)

def inicio(request):

    return render(request, "App/inicio.html")

def usuario(request):
    
    return render(request,"App/user.html")

def soporte(request):

    return render(request,"App/soporte.html")

def conductor(request):

    return render(request,"App/conductor.html")

