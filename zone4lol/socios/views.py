from django.shortcuts import render, redirect
from django.http import HttpResponse
from socios.models import Socio
from django.contrib.auth.models import User
import datetime
from socios.forms import SocioForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

def fecha_actual(request):
    hoy=datetime.datetime.now()
    html="<html><body>Hoy es %s.</body></html>" % hoy
    return HttpResponse(html)

def socios(request):
    lista_socios= Socio.objects.order_by('-nombre')
    context={'socios':lista_socios}
    return render(request, 'socios/index.html', context)

def socios_lista(request):
    lista_socios= Socio.objects.order_by('id')
    context={'socios':lista_socios}
    return render(request, 'socios/listar.html', context)

class socioList(ListView):
    model=Socio
    model=User
    template_name = 'socios/listar.html'

def socios_create(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
        return  redirect('socios_listar')
    else:
        form = SocioForm()

    return render(request, 'socios/socio_form.html', {'form':form})
def socio_edit(request, id_socio):
    socio = Socio.objects.get(id=id_socio)
    if request.method == 'GET':
        form = SocioForm(instance=socio)
    else:
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
        return redirect('socios_listar')
    return render(request, 'socios/socio_form.html', {'form':form})


def socio_delete(request, id_socio):
    socio = Socio.objects.get(id=id_socio)
    context={'socios': socio}
    if request.method == 'POST':
        socio.delete()
        return redirect('socios_listar')
    return render(request, 'socios/socio_delete.html', context)

class socioCreate(CreateView):
    model = Socio
    form_class = SocioForm
    template_name = 'socios/socio_form.html'
    success_url = reverse_lazy('socios_listar')

class socioUpdate(UpdateView):
    model = Socio
    form_class = SocioForm
    template_name = 'socios/socio_form.html'
    success_url = reverse_lazy('socios_listar')

class socioDelete(DeleteView):
    model = Socio
    template_name = 'socios/socio_delete.html'
    success_url = reverse_lazy('socios_listar')