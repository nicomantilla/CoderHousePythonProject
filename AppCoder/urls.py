from django.urls import path
from AppCoder import views
urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("user", views.usuario, name="usuario"),
    path("soporte", views.soporte, name="soporte"),
    path("conductor", views.conductor, name="conductor"),
    path("login", views.login_request, name="Login"),
] 
