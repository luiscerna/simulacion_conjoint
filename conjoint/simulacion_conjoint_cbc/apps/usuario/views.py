from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.generic import ListView, View, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render

from apps.usuario.forms import RegistroForm
# Create your views here.



class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registro.html"
	form_class = RegistroForm
	success_url = reverse_lazy('usuario:usuario_list')
	
class UsuarioList(ListView):
	model = User
	template_name = "usuario/usuario_list.html"
	paginate_by = 6

class UsuarioUpdate(UpdateView):
	model = User
	form_class = RegistroForm
	template_name = 'usuario/registro.html'
	success_url = reverse_lazy('usuario:usuario_list')

class UsuarioDelete(DeleteView):
	model=User
	template_name = 'usuario/usuario_delete.html'
	success_url = reverse_lazy('usuario:usuario_list')