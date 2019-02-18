from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from foro.models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from foro.forms import *

# Create your views here.

class forosList(ListView):
    model = Foro
    template_name = 'foros/listar.html'


class foroCreate(CreateView):
    model = Foro
    form_class = foroForm
    template_name = 'foros/foroForm.html'
    success_url = reverse_lazy('foros_listar')

class foroDelete(DeleteView):
    model = Foro
    template_name = 'foros/foro_delete.html'
    success_url = reverse_lazy('foros_listar')

class postDelete(DeleteView):
    model = Post
    template_name = 'foros/post_delete.html'
    success_url = reverse_lazy('foros_listar')


def postForo(request, pk):
    id=pk
    posts = Post.objects.filter(foro=id).order_by('-created')
    foro = Foro.objects.filter(id=id)
    context={'lista_posts':posts,'lista_foros': foro}
    return render(request, 'foros/listar_posts.html', context)

def postCreate(request, pk):
    if request.method == 'POST':
        Commentform = postForm(request.POST)
        if Commentform.is_valid():
            titulo = request.POST.get('titulo')
            contenido = request.POST.get('contenido')
            foro1 = Foro.objects.get(id=pk)
            post=Post.objects.create(titulo=titulo, contenido=contenido, foro=foro1, autor=request.user)
            post.save()
            return HttpResponseRedirect(reverse('posts_listar', args=(pk,)))
    else:
        form = postForm()

    return render(request, 'foros/posts_form.html', {'form':form})