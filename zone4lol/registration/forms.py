from django.contrib.auth.models import User
from socios.models import Socio
from django  import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electronico',
        }

class SocioForm(forms.ModelForm):

    class Meta:
        model = Socio



        fields = [
            'nombre_sum',
            'localidad',
            'socio',
            'imagen',
        ]
        labels={
            'nombre_sum':'Nombre de invocador',
            'localidad':'Localidad',
            'imagen': 'Imagen de perfil (Puedes elegirla mas tarde)',
            'socio': '¿Quieres ser socio?',
        }
        widgets={
            'imagen': forms.ClearableFileInput(),
            'nombre_sum': forms.TextInput(attrs={'class': 'form-control', 'style': 'border-radius: 5rem;', 'minlength': '5'}),
            'localidad': forms.TextInput(attrs={'class': 'form-control', 'style': 'border-radius: 5rem;', 'minlength': '5'}),
        }

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        exclude = [
            'password',
        ]
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electronico',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'border-radius: 5rem;', 'minlength': '5'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'style': 'border-radius: 5rem;', 'minlength': '5'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'border-radius: 5rem;', 'minlength': '5'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'style': 'border-radius: 5rem;', 'minlength': '5'}),
        }