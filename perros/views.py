from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import models
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Perro
from .forms import PerroForm, PerroEditarForm, PerroModerarForm

#Importando lo necesario para el rest
from rest_framework import generics #Modelo de View que devuelve JSON
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response #Cosa magica que devuelve JSON ante la solicitud
from rest_framework import status
from .serializers import PerroSerializer

# Variables de mensajes
EXITO = 25
exitoAlSubir = '¡Subiste un perro con éxito! Se envió a moderación, estará listo cuanto antes'
exitoAlEditar = '¡El perro ha sido modificado con éxito!'
exitoAlModerar = 'El perro ha sido aprobado, ahora será mostrado en la lista'
exitoAlEliminar = 'Has eliminado el perro con éxito. No será mostrado en lista.'


# Views.

#Index - Landing Page
def perros_inicio(request):
	#queryset = Perro.objects.filter(encontro_casa=False)
	context = {
	}
	return render(request, "inicio.html", context)

#RETRIEVE - Lista de perros
def perros_display(request):
    # Abriendo un deposito para los mensajes
	mensajes = messages.get_messages(request)
	queryset = Perro.objects.filter(encontro_casa=False, aprobado=True)
	context = {
    # Anadiendo mensajes al context
		"mensajes": mensajes,
		"queryset": queryset,
	}
	return render(request, "lista.html", context)


#CREATE - Creacion de perro (objeto)
def perros_subir(request):
	#CONDICION: El usuario debe estar logueado para acceder al formualrio de cracion
	if request.user.is_authenticated():
		form = PerroForm(request.POST, request.FILES or None)
		#Si el formulario es valido (esta lleno)
		if request.method == "POST":
			if form.is_valid():
				instance = form.save(commit=False)
				#Se guarda como objeto
				instance.save()
                # Anadiendo mensaje de exito en lista de perros
				messages.add_message(request, EXITO, exitoAlSubir)
				#Posteriormente se redirecciona a la lista
				return HttpResponseRedirect(reverse('perros:lista'))

		context = {
			"form": form,
		}
		return render(request, "subir.html", context)
	else:
		return HttpResponseRedirect(reverse('account_login'))

#DELETE - Borrar perro
class perros_borrar(DeleteView):
	model = Perro
	success_url = reverse_lazy('perros:lista')

class perros_borrar_moderacion(DeleteView):
	model = Perro
	success_url = reverse_lazy('perros:lista')

#UPDATE - Actualizar perro
def perros_actualizar(request, id=None):
	#Retrieving ID and author of the post. Only the author can modify the post
	instance = get_object_or_404(Perro, id=id, author=request.user)
	#Importando el formulario del perro, rellenandolo con la instance definida anteriormente
	form = PerroEditarForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.add_message(request, EXITO, exitoAlEditar)
		return HttpResponseRedirect(reverse('perros:lista'))

	context = {
		"perroDetalle": instance,
		"form": form,
		#"perroDetalle": Perro.objects.get(id=id)
	}
	return render(request, "editar.html", context)

#RETRIEVE2
def perros_detalles(request, id):
	pe = Perro.objects.get(id=id)
	usuario = pe.author.first_name + " " + pe.author.last_name
	perro = get_object_or_404(Perro, id=id)
	context = {
		"perroDetalle": perro,
		#Solicitando nombre y apellido del autor
		"subido": perro.author.first_name + " " + perro.author.last_name,
		#"perroDetalle": Perro.objects.get(id=id)
	}
	return render(request, "detalles.html", context)


#Moderacion
def perros_moderacion(request):
	if request.user.is_superuser:
		queryset = Perro.objects.filter(encontro_casa=False)
		context = {
			"queryset": queryset,
		}
		return render (request, "moderacion.html", context)
	else:
		return HttpResponseRedirect(reverse('perros:inicio'))

def perros_moderacion_editar(request, pk=None):
	#Retrieving ID and author of the post. Only the author can modify the post
	instance = get_object_or_404(Perro, pk=pk, author=request.user)
	#Importando el formulario del perro, rellenandolo con la instance definida anteriormente
	form = PerroModerarForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.add_message(request, EXITO, exitoAlModerar)
		return HttpResponseRedirect(reverse('perros:lista'))

	context = {
		"perroDetalle": instance,
		"form": form,
		#"perroDetalle": Perro.objects.get(id=id)
	}
	return render(request, "editar-moderacion.html", context)

##### RESTful

#Hace lista de todos los perros, o crea uno nuevo
class perros_api_listar(generics.ListAPIView):
	queryset = Perro.objects.filter(aprobado=False, encontro_casa=False)
	serializer_class = PerroSerializer #(queryset, many=True)

	def perform_create(self, serializer):
		serializer.save

# class perros_api(generics.ListCreateAPIView):
#
# 	queryset = Perro.objects.filter(aprobado=False, encontro_casa=False)
# 	serializer_class = PerroSerializer #(queryset, many=True)
#
# 	def perform_create(self, serializer):
# 		authentication_classes = (TokenAuthentication,)
# 		permission_classes = (IsAuthenticated,)
# 		serializer.save()

class perros_api_crear(generics.CreateAPIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated, )
	serializer_class = PerroSerializer
