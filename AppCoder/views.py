import re
from tkinter import EW
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import is_valid_path
from AppCoder.models import Soporte, Usuario, Conductor, Inicio
# from AppCoder.forms import FormularioInicio
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

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

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])
            
            if user is not None:
                login(request, user)
                return render(request, "App/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            
            else:
                return render(request, "App/inicio.html", {"mensaje":"Error, datos incorrectos"})
        
        else:
                return render(request, "App/inicio.html", {"mensaje":"Error, formulario erroneo"})
    
    form = AuthenticationForm()
    return render(request, "App/login.html", {"form":form})

# return render(request,"App/iniciar.html")