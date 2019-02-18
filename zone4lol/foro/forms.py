from django  import forms
from django.forms import Textarea
from foro.models import *

class foroForm(forms.ModelForm):
    class Meta:
        model = Foro

        fields = [
            'nombre',
        ]
        label = {
            'nombre' : 'Titulo del Foro',

        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'style':'border-radius: 5rem;','minlength':'5', 'style':'border:1px solid black;'}),
        }

class postForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = [
            'titulo',
            'contenido',
        ]
        label = {
            'titulo': 'Titulo del post',
            'contenido': 'Escribe aqui',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),

        }