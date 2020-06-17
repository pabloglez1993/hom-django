"""HogaresYObrasMexicanas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from HogaresYObrasMexicanas.views import *#HomeView,ProyectosViewSet,PartidasViewSet

router = routers.DefaultRouter()
router.register(r"proyectos",ProyectosViewSet)
router.register(r"partidas",PartidasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    #displays
    path('', HomeView.as_view()),
    path('proyecto/partidas/',PartidasDisplay.as_view()),
    path('proyecto/partidas/conceptos/',ConceptosDisplay.as_view()),
    path('proyecto/partidas/conceptos/unidades/',UnidadesDisplay.as_view()),
    #registros
    path('registro/proyecto/',RegistroProyectoDisplay.as_view()),
    path('registro/partida/',RegistroPartidaDisplay.as_view()),
    path('registro/concepto/',RegistroConceptoDisplay.as_view()),
    path('registro/unidad/',RegistroUnidadeDisplay.as_view()),
    #edit
    path('editar/proyecto',EditProyectoDisplay.as_view()),
    path('editar/partida',EditPartidaDisplay.as_view()),
    path('editar/concepto',EditConceptoDisplay.as_view()),
    path('editar/unidad',EditUnidadDisplay.as_view()),
]
