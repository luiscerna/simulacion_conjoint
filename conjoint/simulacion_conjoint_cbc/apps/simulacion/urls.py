from django.urls import path, re_path
from apps.simulacion.views import Index, SimulacionCreate, SimulacionList, SimulacionShow, SimulacionUpdate, \
 SimulacionDelete, AtributoCreate, EncuestaList, EncuestaShow, AtributoUpdate, AtributoDelete, NivelCreate, NivelUpdate, \
 NivelDelete, PerfilCreate, PerfilUpdate, PerfilDelete, DetallePerfilCreate, SelectAtributoList, SimulacionShowTabla, DetallePerfilDelete
from apps.simulacion import views
from django.contrib.auth.decorators import login_required

app_name = "simulacion"

urlpatterns = [
	path('registrar/', login_required(SimulacionCreate.as_view()), name="registrar"),
	path('listar/', login_required(SimulacionList.as_view()), name="simulacion_listar"),
	path('mostrar/<pk>/', login_required(SimulacionShow.as_view()), name="simulacion_mostrar"),
	path('editar/<pk>/', login_required(SimulacionUpdate.as_view()), name="simulacion_editar"),
	path('eliminar/<pk>/', login_required(SimulacionDelete.as_view()), name="simulacion_eliminar"),
	path('registrar_atributo/<pk>/', login_required(AtributoCreate.as_view()), name="registrar_atributo"),
	path('editar_atributo/<pk>/<pk_1>/', login_required(AtributoUpdate.as_view()), name="editar_atributo"),
	path('eliminar_atributo/<pk>/<pk_1>/', login_required(AtributoDelete.as_view()), name="eliminar_atributo"),
	path('registrar_nivel/<pk>/<pk_1>/', login_required(NivelCreate.as_view()), name="registrar_nivel"),
	path('editar_nivel/<pk>/<pk_1>/', login_required(NivelUpdate.as_view()), name="editar_nivel"),
	path('eliminar_nivel/<pk>/<pk_1>/', login_required(NivelDelete.as_view()), name="eliminar_nivel"),
	path('registrar_perfil/<pk>/', login_required(PerfilCreate.as_view()), name="registrar_perfil"),
	path('editar_perfil/<pk>/<pk_1>/', login_required(PerfilUpdate.as_view()), name="editar_perfil"),
	path('eliminar_perfil/<pk>/<pk_1>/', login_required(PerfilDelete.as_view()), name="eliminar_perfil"),
	path('registrar_detalle_perfil/<pk>/<pk_1>/', login_required(DetallePerfilCreate.as_view()), name="registrar_detalle_perfil"),
    path('eliminar_detalle_perfil/<pk>/<pk_1>/', login_required(DetallePerfilDelete.as_view()), name="eliminar_detalle_perfil"),
	path('editar_perfil/<pk>/<pk_1>/', login_required(PerfilUpdate.as_view()), name="editar_perfil"),
	path('eliminar_perfil/<pk>/<pk_1>/', login_required(PerfilDelete.as_view()), name="eliminar_perfil"),
	path('seleccionar_atributo/<pk>/<pk_1>/', login_required(SelectAtributoList.as_view()), name="seleccionar_atributo"),
	path('encuesta/<pk>/', EncuestaShow.as_view(), name="encuesta"),
	path('resultados/tabla/<pk>/', login_required(SimulacionShowTabla.as_view()), name="resultado"),

]
