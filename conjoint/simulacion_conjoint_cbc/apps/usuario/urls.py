from django.urls import path
from apps.usuario.views import RegistroUsuario, UsuarioList, UsuarioUpdate, UsuarioDelete
from django.contrib.auth.decorators import login_required
app_name = "usuario"

urlpatterns = [
	path('registrar/', login_required(RegistroUsuario.as_view()), name="usuario_register"),
	path('listar/', login_required(UsuarioList.as_view()), name="usuario_list"),
	path('editar/<pk>/', login_required(UsuarioUpdate.as_view()), name="usuario_edit"),
	path('eliminar/<pk>/', login_required(UsuarioDelete.as_view()), name='usuario_delete'),
	
	#path('registrar/', RegistroUsuario.as_view(), name="registrar"),
]
