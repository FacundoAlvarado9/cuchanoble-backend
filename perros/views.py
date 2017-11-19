from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import models

from .models import Perro
from .forms import PerroForm
from .forms import PerroEditarForm

# Views.

#Index - Landing Page
def perros_inicio(request):
	#queryset = Perro.objects.filter(encontro_casa=False)
	context = {
	}
	return render(request, "inicio.html", context)

#RETRIEVE - Lista de perros
def perros_display(request):
	queryset = Perro.objects.filter(encontro_casa=False)
	context = {
		"queryset": queryset,
	}
	return render(request, "lista.html", context)


#CREATE - Creacion de perro (objeto)
def perros_subir(request):
	#CONDICION: El usuario debe estar logueado para acceder al formualrio de cracion
	if request.user.is_authenticated():
		form = PerroForm(request.POST or None)
		#Si el formulario es valido (esta lleno)
		if form.is_valid():
			instance = form.save(commit=False)
			#Se guarda como objeto
			instance.save()
			#Posteriormente se redirecciona a la lista
			return HttpResponseRedirect(reverse('perros:lista'))

		context = {
			"form": form,
		}
		return render(request, "subir.html", context)
	else:
		return HttpResponseRedirect(reverse('account_login'))

#TODO: Borrar perro
def perros_borrar(request):
	return HttpResponse("<h1>Hello</h1>")

#UPDATE - Actualizar perro
def perros_actualizar(request, id=None):
	#Retrieving ID and author of the post. Only the author can modify the post
	instance = get_object_or_404(Perro, id=id, author=request.user)
	#Importando el formulario del perro, rellenandolo con la instance definida anteriormente
	form = PerroEditarForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(reverse('perros:lista'))

	context = {
		"perroDetalle": instance,
		"form": form,
		#"perroDetalle": Perro.objects.get(id=id)
	}
	return render(request, "subir.html", context)

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
