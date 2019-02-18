from django  import forms
from eventos.models import Evento
from socios.models import Socio


class eventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo',
                  'descripcion',
                  'fecha_inic',
                  'limite_ayu',
                  'link',
                  'ayudantes',
        ]
        labels = {
            'titulo': 'Titulo del evento',
            'descripcion': 'Descripcion',
            'fecha_inic': 'Fecha Inicio',
            'limite_ayu': 'Vacantes para voluntarios',
            'link': 'Enlace de inscripcion',
            'ayudantes': 'Voluntarios',
        }
        widgets={
            'titulo' : forms.TextInput(attrs={'class':'form-control', 'style':'border-radius: 5rem;','minlength':'5'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'style':'border-radius: 5rem;'}),
            'limite_ayu': forms.NumberInput(attrs={'class': 'form-control', 'style':'border-radius: 5rem;'}),
            'fecha_inic': forms.SelectDateWidget(),
            'ayudantes' : forms.CheckboxSelectMultiple(),
        }


