from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Foro(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def countPosts(self):
        count = self.postForo.all().count
        return count

class Post(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.TextField(max_length=500)
    foro = models.ForeignKey(Foro, on_delete=models.CASCADE, related_name='postForo')
    autor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, default='AutorEliminado', related_name='autorPost')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

