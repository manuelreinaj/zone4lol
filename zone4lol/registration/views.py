from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, request
from socios.models import Socio
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from registration.forms import RegistrationForm, SocioForm, UserForm
from django.shortcuts import redirect

# Create your views here.

class detalleUser(DetailView):
    model = User
    template_name = 'socios/detalle_socio.html'


    #def get_context_data(self, *args, **kwargs):
     #   pk = self.kwargs.get('pk')
     #   context = super(DetalleUser, self).get_context_data(**kwargs)
     #   context['modelo1'] = User.objects.get(pk=pk)
     #   return context



class userList(ListView):
    template_name = 'socios/listar.html'

    def get_context_data(self, *args, **kwargs):
        context = super(userList, self).get_context_data(**kwargs)
        context['modelo1'] = User.objects.get()
        context['modelo2'] = Socio.objects.get()
        return context

class registroUser(CreateView):
    template_name = 'registrations/update_user.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('nosotros')

class userRegister(CreateView):
    model = User
    template_name = 'registrations/signup.html'
    form_class = RegistrationForm
    second_form_class = SocioForm
    success_url = reverse_lazy('nosotros')

    def get_context_data(self, **kwargs):
        context  = super(userRegister, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2  =self.second_form_class(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            socio = form2.save(commit=False)
            socio.user_id = form.save()
            socio.save()
            return HttpResponseRedirect(self.get_success_url())

        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class deleteUser(DeleteView):
    model = User
    template_name= 'socios/socio_delete.html'
    success_url = reverse_lazy('nosotros')


class updateUser(UpdateView):
    model = User
    second_model= Socio
    template_name = 'registrations/update_user.html'
    form_class = UserForm
    second_form_class = SocioForm
    success_url = reverse_lazy('nosotros')

    def get_context_data(self, **kwargs):
        context = super(updateUser, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        user = self.model.objects.get(id=pk)
        socio = self.second_model.objects.get(user_id=user.id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=socio)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        user = self.model.objects.get(id=kwargs['pk'])
        socio = self.second_model.objects.get(user_id=user.id)

        form = self.form_class(request.POST, instance=user)
        form2 = self.second_form_class(request.POST, request.FILES, instance=socio)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return redirect('nosotros')

