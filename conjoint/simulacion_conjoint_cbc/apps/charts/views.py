from django.http import JsonResponse
from apps.simulacion.models import Perfil as PerfilModel, Simulacion as SimulacionModel
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HomeView(View):
	def get(self, request, *args, **kwargs):
		lista_simulacion = SimulacionModel.objects.filter(idSimulacion=self.kwargs['pk'])
		global perfiles
		perfiles = PerfilModel.objects.filter(idSimulacion=lista_simulacion[0].idSimulacion)

		return render(request, 'simulacion/simulacion_chart.html', {})



def get_data(request, *args, **kwargs):
	data = {
		"sales": 100,
		"customers": 10,
	}
	return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []


    def get(self, request, format=None):
    	votos=''
    	nombres=''
    	col1=''
    	col2=''
    	i=0

    	color1=[
    	     'rgba(94, 220, 22, 0.5)',
			 'rgba(89, 162, 190, 0.5)',
			 'rgba(255, 206, 86, 0.5)',
			 'rgba(75, 192, 192, 0.5)',
			 'rgba(153, 102, 255, 0.5)',
			 'rgba(255, 159, 64, 0.5)',
			 'rgba(22, 61, 220, 0.5)',
			 'rgba(74, 138, 17, 0.5)',
			 'rgba(128, 229, 38, 0.5)',
			 'rgba(229, 218, 38, 0.5)',
			 'rgba(229, 128, 38, 0.5)',
			 'rgba(167, 154, 142, 0.5)',
			 'rgba(18, 243, 247, 0.5)']
    	color2=[
    	     'rgba(94, 220, 22, 1)',
			 'rgba(54, 162, 235, 1)',
			 'rgba(255, 206, 86, 1)',
			 'rgba(75, 192, 192, 1)',
			 'rgba(153, 102, 255, 1)',
			 'rgba(255, 159, 64, 1)',
			 'rgba(22, 61, 220, 1)',
			 'rgba(74, 138, 17, 1)',
			 'rgba(128, 229, 38, 1)',
			 'rgba(229, 218, 38, 1)',
			 'rgba(229, 128, 38, 1)',
			 'rgba(167, 154, 142, 1)',
			 'rgba(18, 243, 247, 1)']

    	#perfiles = PerfilModel.objects.filter(idSimulacion=1)
    	#perfiles = PerfilModel.objects.filter(idSimulacion=x)

    	for perfil in perfiles:
    		votos += str(perfil.voto)
    		nombres += perfil.nombre+','

    	t_nombres=nombres.split(',')
    	t_votos=[int(voto) for voto in votos]

    	while i < len(t_votos):
    		col1 += color1[i]+'/'
    		col2 += color2[i]+'/'
    		i = i + 1

    	labels = t_nombres
    	default_items=t_votos
    	color1=col1.split('/')
    	color2=col2.split('/')
    	data = {"labels": labels,
    			"default": default_items,
    			"backColor": color1,
    			"borColor": color2,
    	}
    	return Response(data)
