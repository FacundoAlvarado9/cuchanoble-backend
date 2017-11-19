from django.db import models
from django.contrib.auth.models import User
from author.decorators import with_author


# Create your models here.
TAMANO_CHOICES = (
	('Muy g rande', 'MUY GRANDE'),
	('Grande', 'GRANDE'),
	('Mediano',' MEDIANO'),
	('Chico', 'CHICO'),
	('Muy chico', 'MUY CHICO'),
	)

ESTADO_CHOICES = (
	('Excelente estado', 'EXCELENTE ESTADO'),
	('Buen estado', 'BUEN ESTADO'),
	('Lastimado', 'LASTIMADO'),
	('Mal estado', 'MAL ESTADO'),
	)

SEXO_CHOICES = (
	('Macho', 'MACHO'),
	('Hembra', 'HEMBRA'),
	)

EDAD_CHOICES = (
	('Cachorro', 'CACHORRO'),
	('Adulto', 'ADULTO'),
	)


@with_author
class Perro(models.Model):
	direccion = models.CharField('Zona (Barrio)', max_length=250)
	sexo = models.CharField(max_length=10, choices=SEXO_CHOICES, null=True)
	edad = models.CharField(max_length=8, choices=EDAD_CHOICES, null=True)
	tamano = models.CharField(max_length=15, choices=TAMANO_CHOICES, default='mediano')
	estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='buen estado')
	contacto = models.CharField(max_length=15, default='')
	subido_por = models.CharField(max_length=50, null=True)
	encontro_casa = models.BooleanField(default=False)
	subido_el = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado_el = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.direccion + "-" + self.estado

	def get_absolute_url(self):
		return reverse("perros:detalles", kwargs={"id": self.id})

	def editar_perro(self):
		return reverse("perros:editar", kwargs={"id": self.id})
