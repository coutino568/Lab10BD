from django.db import models
from django.conf import settings
from canciones.models import Cancion

# Create your models here.
class Playlist(models.Model):
    id = models.AutoField(primary_key=True)
    username_usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username_usuario','nombre'], name='playlist unica')    
        ]

class Esta_en(models.Model):
    id_playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    id_cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_playlist','id_cancion'], name='cancion unica en playlist')    
        ]
