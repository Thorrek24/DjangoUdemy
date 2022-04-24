from django.db import models

# Create your models here.

class Registrado(models.Model):
    nombre = models.CharField(max_length=100)#, blank=True, null=True si añadimos estos dos campos
                                            # hacemos que no sea obligatorio rellenarlo
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self): #Python2
        return self.nombre

    def __str__(self): #Python3
        return self.nombre