from django.contrib import admin

from .models import Perro

class PerrosAdmin(admin.ModelAdmin):
	list_display = ('direccion' , 'estado', 'contacto', 'id', 'author')
	list_filter = ('direccion',)
	class Meta:
		model = Perro

admin.site.register(Perro, PerrosAdmin)