from django.shortcuts import render
from eventos.models import Evento
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from eventos.forms import eventoForm
# Create your views here.

def eventos_lista(request):
    evento = Evento.objects.order_by('fecha_inic')
    return render(request, 'eventos/listar.html',{'eventos': evento})

class eventosList(ListView):
    model = Evento
    template_name = 'eventos/listar.html'


class eventoCreate(CreateView):
    model = Evento
    form_class = eventoForm
    template_name = 'eventos/evento_form.html'
    success_url = reverse_lazy('eventos_listar')

class eventoUpdate(UpdateView):
    model = Evento
    form_class = eventoForm
    template_name = 'eventos/evento_form.html'
    success_url = reverse_lazy('eventos_listar')

class eventoDelete(DeleteView):
    model = Evento
    template_name = 'eventos/evento_delete.html'
    success_url = reverse_lazy('eventos_listar')