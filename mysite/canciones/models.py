from django.db import models
from django.conf import settings
import datetime

# Create your models here.
class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    id_genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    username_usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    fecha_publicacion = models.DateField(default=datetime.date.today)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['titulo','username_usuario'], name='album unico por artista')    
        ]
        
    def __str__(self):
        return self.titulo

class Cancion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_album = models.ForeignKey(Album,on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    fecha_publicacion = models.DateField(default=datetime.date.today)
    link = models.URLField(max_length=200, unique=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nombre','id_album'], name='cancion unica')    
        ]




    
class Escuchar(models.Model):
    username_usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    id_cancion = models.ForeignKey(Cancion,on_delete=models.CASCADE)
    fecha_reproduccion = models.DateField(default=datetime.date.today)
    