from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class SimulacionEstado(models.Model):
    idSimulacionEstado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.estado)

class Simulacion(models.Model):
    idSimulacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    producto = models.CharField(max_length=75, null=True)
    nombreEncuesta = models.CharField(max_length=75, null=True)
    preguntaEncuesta = models.CharField(max_length=300, null=True)
    idSimulacionEstado = models.ForeignKey(SimulacionEstado, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.idSimulacion)

    def get_absolute_url(self):
        return reverse_lazy('simulacion:simulacion_mostrar', kwargs={'pk': self.pk})

class Atributo(models.Model):
    idAtributo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    idSimulacion = models.ForeignKey(Simulacion, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)

class Nivel(models.Model):
    idNivel = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    idAtributo = models.ForeignKey(Atributo, null=True, on_delete=models.CASCADE, related_name='nivel')

    def __str__(self):
        return '{}'.format(self.nombre)

class Perfil(models.Model):
    idPerfil = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    voto = models.IntegerField(default=0)
    media = models.ImageField(upload_to='static/img', blank=True)
    idSimulacion = models.ForeignKey(Simulacion, null=True, on_delete=models.CASCADE, related_name='perfil')

    def __str__(self):
        return '{}'.format(self.nombre)

class DetallePerfil(models.Model):
    idDetallePerfil = models.AutoField(primary_key=True)
    idPerfil = models.ForeignKey(Perfil, null=True, on_delete=models.CASCADE, related_name='detalleperfil')
    idNivel = models.ForeignKey(Nivel, null=True, on_delete=models.CASCADE, related_name='detalleperfil')
