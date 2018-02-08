from django import forms
from .models import Perro

class PerroForm(forms.ModelForm, forms.Form):
	class Meta:
		model = Perro
		fields = [
			"direccion",
			"sexo",
			"edad",
			"tamano",
			"estado",
			'contacto',
			'imagen',
			#"encontro_casa",
		]

class PerroEditarForm(forms.ModelForm, forms.Form):
	class Meta:
		model = Perro
		fields = [
			"direccion",
			"sexo",
			"edad",
			"tamano",
			"estado",
			'contacto',
			"encontro_casa",
		]




# Custom signup form ALLAUTH
class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='Nombre')
    last_name = forms.CharField(max_length=30, label='Apellido')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
