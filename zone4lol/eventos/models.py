from django.db import models
from socios.models import Socio

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    fecha_inic = models.DateField()
    limite_ayu = models.IntegerField()
    link = models.URLField(max_length=500, unique=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ayudantes = models.ManyToManyField(Socio, related_name='eventos')

    def Meta(self):
        verbose_name_plural='Eventos'
        ordering=['created']

    def __str__(self):
        return self.titulo