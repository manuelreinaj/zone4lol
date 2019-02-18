from django  import forms
from socios.models import Socio

class SocioForm(forms.ModelForm):

    class Meta:
        model = Socio

        fields = [
            'localidad',
            'socio',

        ]
        labels={
            'localidad':'Localidad',
            'socio':'Socio',
            'imagen':'Imagen de perfil'
        }
        widgets={
            'localidad': forms.TextInput(attrs={'class':'form-control'}),
            'socio': forms.CheckboxInput(),
        }