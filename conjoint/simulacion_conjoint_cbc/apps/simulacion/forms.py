from apps.simulacion.models import Simulacion, Atributo, Nivel, Perfil, DetallePerfil
from django import forms

class SimulacionForm(forms.ModelForm):
    class Meta:
        model = Simulacion
        fields = [
            'nombre',
            'producto',
            'nombreEncuesta',
            'preguntaEncuesta',
            'idSimulacionEstado',
        ]

        labels = {
            'nombre': 'Nombre de Simulación',
            'producto': 'Producto',
            'nombreEncuesta': 'Nombre de la Encuesta',
            'preguntaEncuesta': 'Pregunta de la Encuesta',
            'idSimulacionEstado': 'Estado',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'producto': forms.TextInput(attrs={'class':'form-control'}),
            'nombreEncuesta': forms.TextInput(attrs={'class':'form-control'}),
            'preguntaEncuesta': forms.TextInput(attrs={'class':'form-control'}),
            'idSimulacionEstado': forms.Select(attrs={'class':'form-control'}),
        }

class AtributoForm(forms.ModelForm):
    class Meta:
        model = Atributo
        fields = [
            'nombre',
        ]

        labels = {
            'nombre': 'Nombre',
        }

        widgets = {
            'nombre': forms.TextInput(),
        }

class NivelForm(forms.ModelForm):
    class Meta:
        model = Nivel
        fields = [
            'nombre',
        ]

        labels = {
            'nombre': 'Nombre',
        }

        widgets = {
            'nombre': forms.TextInput(),
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'nombre',
            'media',
        ]

        labels = {
            'nombre': 'Nombre de Perfil',
            'media': 'Seleccionar imagen',
        }

        widgets = {
            'nombre': forms.TextInput(),
        }

class DetallePerfilForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super(DetallePerfilForm, self).__init__(*args, **kwargs)
        self.fields['idNivel'].queryset = Nivel.objects.filter(idAtributo=request.GET.get("atributo"))

    class Meta:
        model = DetallePerfil
        fields = [
            'idNivel',
        ]

        labels = {
            'idNivel': 'Nivel de Relación',
        }

#class RespuestaForm(forms.ModelForm):
#    class Meta:
#        model = Respuesta
#        fields = [
#            'idPerfil',
#        ]
#
#        widgets = {
#            'idNivel': forms.RadioSelect(),
#        }
