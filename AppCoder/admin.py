from django.contrib import admin
from AppCoder.models import Conductor, Inicio, Soporte, Usuario

admin.site.register(Conductor)
admin.site.register(Usuario)
admin.site.register(Soporte)
admin.site.register(Inicio)