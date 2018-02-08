"""cuchanoble URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
  perros_display,
  perros_subir,
  perros_borrar,
  perros_actualizar,
  perros_detalles,
  perros_inicio,
  PerroList,
  PerroListCreate,
  )


urlpatterns = [

   	#CRUD
    url(r'^$', perros_inicio, name='index'),
    url(r'^perros/$', perros_display, name='lista'),
    url(r'^detalles/(?P<id>\d+)/$', perros_detalles, name='detalles'),
    url(r'^subir/$', perros_subir, name='subir'),
    url(r'^borrar/$', perros_borrar, name='borrar'),
    url(r'^editar/(?P<id>\d+)/$', perros_actualizar, name='editar'),
    url(r'^json/$', PerroList.as_view()),
    url(r'^jsoncreate/$', PerroListCreate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
