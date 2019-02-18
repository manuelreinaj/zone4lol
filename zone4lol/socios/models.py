from django.db import models
from django.contrib.auth.models import User
from zone4lol import settings

# Create your models here.

class Socio(models.Model):
    user_id= models.OneToOneField(User, on_delete=models.CASCADE, default=999)
    nombre_sum = models.CharField(max_length=50, null=True)
    imagen = models.FileField(upload_to='usuarios/', default='default/user1.png')
    localidad = models.CharField(max_length=50)
    socio=models.BooleanField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id.first_name+' '+self.user_id.last_name



#class Participa(models.Model):
 #   id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
 #   id_socio = models.ForeignKey(Socio,on_delete=models.CASCADE)