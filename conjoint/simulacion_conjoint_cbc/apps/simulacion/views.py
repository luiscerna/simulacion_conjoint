from django.shortcuts import render
from apps.simulacion.models import Simulacion as SimulacionModel, Atributo as AtributoModel, Nivel as NivelModel, Perfil as PerfilModel, DetallePerfil as DetallePerfilModel
from apps.simulacion.forms import SimulacionForm, AtributoForm, NivelForm, PerfilForm, DetallePerfilForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
class SimulacionCreate(CreateView):
	model = SimulacionModel
	form_class = SimulacionForm
	template_name = 'simulacion/simulacion_registrar.html'
	success_url = reverse_lazy('simulacion:simulacion_listar')

class SimulacionList(ListView):
    queryset = SimulacionModel.objects.order_by("idSimulacion")
    template_name = 'simulacion/simulacion_list.html'

class SimulacionShow(ListView):
	model = SimulacionModel
	template_name = 'simulacion/simulacion_show.html'

	def get_context_data(self, **kwargs):
		context = super(SimulacionShow, self).get_context_data(**kwargs)
		lista_simulacion = SimulacionModel.objects.filter(idSimulacion=self.kwargs['pk'])
		lista_atributo = AtributoModel.objects.filter(idSimulacion=lista_simulacion[0].idSimulacion)

		context["lista_simulacion"] = lista_simulacion
		context["lista_atributo"] = lista_atributo
		return context

class SimulacionUpdate(UpdateView):
	model = SimulacionModel
	form_class = SimulacionForm
	template_name = 'simulacion/simulacion_registrar.html'

	def get_context_data(self, **kwargs):
		context = super(SimulacionUpdate, self).get_context_data(**kwargs)
		context['pk'] = self.kwargs['pk']
		return context

class SimulacionDelete(DeleteView):
    model = SimulacionModel
    template_name = 'simulacion/simulacion_delete.html'
    success_url = reverse_lazy('simulacion:simulacion_listar')

class Simulacion(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'simulacion/simulacion.html', {})

class Index(View):
	def get(self, request, *args, **kwargs):
		lista_simulacion = SimulacionModel.objects.all()
		context = {
			'lista_simulacion': lista_simulacion
		}
		return render(request, 'index.html', context)

class AtributoCreate(CreateView):
	model = AtributoModel
	form_class = AtributoForm
	template_name = 'simulacion/simulacion_registro_atributo.html'

	def form_valid(self, form):
	    form.instance.idSimulacion = SimulacionModel.objects.get(idSimulacion=self.kwargs['pk'])
	    return super(AtributoCreate, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('simulacion:simulacion_mostrar', kwargs={'pk': self.kwargs['pk']})

	def get_context_data(self, **kwargs):
		context = super(AtributoCreate, self).get_context_data(**kwargs)
		context['pk'] = self.kwargs['pk']
		return context

class AtributoUpdate(UpdateView):
	model = AtributoModel
	form_class = AtributoForm
	template_name = 'simulacion/simulacion_registro_atributo.html'

	def get_context_data(self, **kwargs):
		context = super(AtributoUpdate, self).get_context_data(**kwargs)
		context['pk_1'] = self.kwargs['pk_1']
		return context

	def get_success_url(self):
		return reverse_lazy('simulacion:simulacion_mostrar', kwargs={'pk': self.kwargs['pk_1']})

class AtributoDelete(DeleteView):
    model = AtributoModel
    template_name = 'simulacion/simulacion_atributo_delete.html'

    def get_success_url(self):
        return reverse_lazy('simulacion:simulacion_mostrar', kwargs={'pk': self.kwargs['pk_1']})

class NivelCreate(CreateView):
	model = NivelModel
	form_class = NivelForm
	template_name = 'simulacion/simulacion_registro_nivel.html'

	def form_valid(self, form):
	    form.instance.idAtributo = AtributoModel.objects.get(idAtributo=self.kwargs['pk'])
	    return super(NivelCreate, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(NivelCreate, self).get_context_data(**kwargs)
		context['pk_1'] = self.kwargs['pk_1']
		return context

	def get_success_url(self):
		return reverse_lazy('simulacion:simulacion_mostrar', kwargs={'pk': self.kwargs['pk_1']})

class NivelUpdate(UpdateView):
	model = NivelModel
	form_class = form_class = NivelForm
	template_name = 'simulacion/simulacion_registro_nivel.html'

	def get_context_data(self, **kwargs):
		context = super(NivelUpdate, self).get_context_data(**kwargs)
		context['pk'] = self.kwargs['pk_1']
		return context

	def get_success_url(self):
		return reverse_lazy('simulacion:simulacion_mostrar', kwargs={'pk': self.kwargs['pk_1']})

class NivelDelete(DeleteView):
    model = NivelModel
    template_name = 'simulacion/simulacion_nivel_delete.html'

    def get_context_data(self, **kwargs):
	    context = super(NivelDelete, self).get_context_data(**kwargs)
	    context["pk_1"] = self.kwargs['pk_1']
	    return context

    def get_success_url(self):
        return reverse_lazy('simulacion:simulacion_mostrar', kwargs={'pk': self.kwargs['pk_1']})

class PerfilCreate(CreateView):
	model = PerfilModel
	form_class = PerfilForm
	template_name = 'simulacion/simulacion_registro_perfil.html'

	def form_valid(self, form):
	    form.instance.idSimulacion = SimulacionModel.objects.get(idSimulacion=self.kwargs['pk'])
	    return super(PerfilCreate, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('simulacion:simulacion_mostrar', kwargs={'pk': self.kwargs['pk']})

	def get_context_data(self, **kwargs):
	    context = super(PerfilCreate, self).get_context_data(**kwargs)
	    context["pk_1"] = self.kwargs['pk']
	    return context

class PerfilUpdate(UpdateView):
	model = PerfilModel
	form_class = PerfilForm
	template_name = 'simulacion/simulacion_registro_atributo.html'

	def get_context_data(self, **kwargs):
	    context = super(PerfilUpdate, self).get_context_data(**kwargs)
	    context["pk"] = self.kwargs['pk_1']
	    return context

	def get_success_url(self):
		return reverse_lazy('simulacion:simulacion_mostrar', kwargs={'pk': self.kwargs['pk_1']})

class PerfilDelete(DeleteView):
    model = PerfilModel
    template_name = 'simulacion/simulacion_atributo_delete.html'

    def get_success_url(self):
        return reverse_lazy('simulacion:simulacion_mostrar', kwargs={'pk': self.kwargs['pk_1']})

class SelectAtributoList(ListView):
		model = SimulacionModel
		template_name = 'simulacion/seleccionar_atributo.html'

		def get_context_data(self, **kwargs):
			context = super(SelectAtributoList, self).get_context_data(**kwargs)
			lista_simulacion = SimulacionModel.objects.filter(idSimulacion=self.kwargs['pk_1'])
			lista_atributo = AtributoModel.objects.filter(idSimulacion=lista_simulacion[0].idSimulacion)
			context["idPerfil"] = self.kwargs['pk']
			context["idSimulacion"] = self.kwargs['pk_1']
			context["lista_atributo"] = lista_atributo
			return context

class DetallePerfilCreate(CreateView):
	model = DetallePerfilModel
	form_class = DetallePerfilForm
	template_name = 'simulacion/registro_detalle_perfil.html'

	def form_valid(self, form):
	    form.instance.idPerfil = PerfilModel.objects.get(idPerfil=self.kwargs['pk'])
	    return super(DetallePerfilCreate, self).form_valid(form)

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs.update({'request': self.request})
		return kwargs

	def get_context_data(self, **kwargs):
	    context = super(DetallePerfilCreate, self).get_context_data(**kwargs)
	    context["pk"] = self.kwargs['pk_1']
	    return context

	def get_success_url(self):
		return reverse_lazy('simulacion:simulacion_mostrar', kwargs={'pk': self.kwargs['pk_1']})

class DetallePerfilDelete(DeleteView):
    model = DetallePerfilModel
    template_name = 'simulacion/delete_detalle_perfil.html'

    def get_context_data(self, **kwargs):
        context = super(DetallePerfilDelete, self).get_context_data(**kwargs)
        context["pk"] = self.kwargs['pk_1']
        return context

    def get_success_url(self):
        return reverse_lazy('simulacion:simulacion_mostrar', kwargs={'pk': self.kwargs['pk_1']})

class EncuestaList(ListView):
    queryset = SimulacionModel.objects.order_by("idSimulacion")
    template_name = 'encuesta/encuesta.html'
    form_class = AtributoForm

class EncuestaShow(ListView):
	model = SimulacionModel
	template_name = 'encuesta/encuesta_show.html'

	def post(self, request, *args, **kwargs):
		simulacion = SimulacionModel.objects.get(idSimulacion=self.kwargs['pk'])
		try:
			seleccion=request.POST.get('choice')
			perfil=PerfilModel.objects.get(idPerfil=seleccion)
		except:
			return render(request, 'encuesta/encuesta_show.html', {'simulacion': simulacion, 'error_message': 'por favor seleccione una opcion'})
		else:
			perfil.voto +=1
			perfil.save()

			return HttpResponseRedirect(reverse('index'))

	def get_context_data(self, **kwargs):
		context = super(EncuestaShow, self).get_context_data(**kwargs)
		lista_simulacion = SimulacionModel.objects.filter(idSimulacion=self.kwargs['pk'])
		lista_atributo = AtributoModel.objects.filter(idSimulacion=lista_simulacion[0].idSimulacion)

		context["lista_simulacion"] = lista_simulacion
		context["lista_atributo"] = lista_atributo
		return context

class SimulacionShowTabla(ListView):
	model = SimulacionModel
	template_name = 'simulacion/simulacion_tabla.html'

	def get_context_data(self, **kwargs):
		context = super(SimulacionShowTabla, self).get_context_data(**kwargs)
		lista_simulacion = SimulacionModel.objects.filter(idSimulacion=self.kwargs['pk'])
		lista_perfil = PerfilModel.objects.filter(idSimulacion=lista_simulacion[0].idSimulacion)

		context['lista_simulacion'] = lista_simulacion
		context['lista_perfil'] = lista_perfil
		return context
