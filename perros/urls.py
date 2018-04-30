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
from django.conf.urls.static import static
from django.conf import settings
from .views import (
  perros_display,
  perros_subir,
  perros_actualizar,
  perros_detalles,
  perros_inicio,
  perros_borrar,
  perros_moderacion,
  perros_moderacion_editar,
  perros_borrar_moderacion,
  perros_api_listar,
  perros_api_crear,
  )


urlpatterns = [

   	#CRUD
    url(r'^$', perros_inicio, name='index'),
    url(r'^perros/lista/$', perros_display, name='lista'),
    url(r'^perros/detalles/(?P<id>\d+)/$', perros_detalles, name='detalles'),
    url(r'^perros/subir/$', perros_subir, name='subir'),
    url(r'^perros/(?P<pk>\d+)/borrar/$', perros_borrar.as_view(), name='borrar'),
    url(r'^perros/(?P<id>\d+)/editar/$', perros_actualizar, name='editar'),

    # RESTful API
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^perros/api/$', perros_api_listar.as_view()),
    url(r'^perros/api/crear$', perros_api_crear.as_view()),

    # moderacion
    url(r'^perros/moderar/$', perros_moderacion, name='moderacion'),
    url(r'^perros/moderar/(?P<pk>\d+)/$', perros_moderacion_editar, name='editar-mod'),
    url(r'^perros/moderar/(?P<pk>\d+)/borrar$', perros_borrar_moderacion.as_view(), name='borrar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = format_suffix_patterns(urlpatterns)
