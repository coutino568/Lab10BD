from django.contrib import admin
from .models import Cancion, Album, Genero
# Register your models here.

admin.site.register(Cancion)
admin.site.register(Album)
admin.site.register(Genero)