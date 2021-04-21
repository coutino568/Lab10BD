from django.db import models
from django.conf import settings
import datetime

# Create your models here.
class Atributos_extra(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre_artistico = models.CharField(max_length=50, default=False, unique=True)

class Suscripcion(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activa = models.BooleanField(default=False)
    fecha_creacion = models.DateField(default=None, null=True)
    fecha_actualizacion = models.DateField(default=datetime.date.today)
    disponibilidad_de_reproducciones = models.IntegerField(default=3)
    
    def reproducir_musica(self):
        if self.activa == False:
            print(self.fecha_actualizacion)
            print(datetime.date.today())
            if self.fecha_actualizacion < datetime.date.today():
                disponibilidad_de_reproducciones = 3
                self.fecha_actualizacion = datetime.date.today() + datetime.timedelta(days=1)
            if self.disponibilidad_de_reproducciones > 0:
                self.disponibilidad_de_reproducciones - 1
        print(str(self.disponibilidad_de_reproducciones))
        return 1
