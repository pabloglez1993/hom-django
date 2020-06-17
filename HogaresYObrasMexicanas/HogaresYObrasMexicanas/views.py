from django.views.generic import TemplateView
from HogaresYObrasMexicanas.models import Proyecto,Partida,Concepto,Unidad
from rest_framework import viewsets
from HogaresYObrasMexicanas.serializers import ProyectoSerializer,PartidaSerializer

"""
    Display de proyectos, partidas, conceptos y unidades
"""

class HomeView(TemplateView):
    template_name  = 'index.html'
    def get_context_data(self, **kwargs):
        print("get context")
        context = super(HomeView,self).get_context_data(**kwargs)
        context['proyectos'] = Proyecto.objects.all()
        return context

class PartidasDisplay(TemplateView):
    template_name  = 'views/Vista_partidas.html'
    def get_context_data(self, **kwargs):
        print("get context")
        context = super(HomeView,self).get_context_data(**kwargs)
        context['partidas'] = Partida.objects.all()
        return context       

class ConceptosDisplay(TemplateView):
    template_name  = 'views/Vista_conceptos.html'
    def get_context_data(self, **kwargs):
        print("get context")
        context = super(HomeView,self).get_context_data(**kwargs)
        context['conceptos'] = Concepto.objects.all()
        return context

class UnidadesDisplay(TemplateView):
    template_name  = 'views/Vista_unidades.html'
    def get_context_data(self, **kwargs):
        print("get context")
        context = super(HomeView,self).get_context_data(**kwargs)
        context['unidades'] = Unidad.objects.all()
        return context

"""
    Vistas de registro para proyectos, partidas, conceptos y unidades
"""
#falta mandar un contex correcto

class RegistroProyectoDisplay(TemplateView):
    template_name  = 'registrations/Registro-proyecto.html'
    def get_context_data(self, **kwargs):
        print("get context")
        context = super(HomeView,self).get_context_data(**kwargs)
        context['proyectos'] = Proyecto.objects.all()
        return context

class RegistroPartidaDisplay(TemplateView):
    template_name  = 'registrations/Registro-partida.html'
    def get_context_data(self, **kwargs):
        print("get context")
        context = super(HomeView,self).get_context_data(**kwargs)
        context['partidas'] = Partida.objects.all()
        return context 

class RegistroConceptoDisplay(TemplateView):
    template_name  = 'registrations/Registro-concepto.html'
    def get_context_data(self, **kwargs):
        print("get context")
        context = super(HomeView,self).get_context_data(**kwargs)
        context['conceptos'] = Concepto.objects.all()
        return context

class RegistroUnidadeDisplay(TemplateView):
    template_name  = 'registrations/Registro-unidad.html'
    def get_context_data(self, **kwargs):
        print("get context")
        context = super(HomeView,self).get_context_data(**kwargs)
        context['unidades'] = Unidad.objects.all()
        return context

"""
    Vistas de edicion de proyectos, partidas, conceptos y unidades
"""
#falta mandar un contex correcto

class EditProyectoDisplay(TemplateView):
    template_name  = 'editar/Editar-proyecto.html'
    def get_context_data(self, **kwargs):
        print("get context")
        context = super(HomeView,self).get_context_data(**kwargs)
        context['proyectos'] = Proyecto.objects.all()
        return context

class EditPartidaDisplay(TemplateView):
    template_name  = 'editar/Editar-partida.html'
    def get_context_data(self, **kwargs):
        print("get context")
        context = super(HomeView,self).get_context_data(**kwargs)
        context['partidas'] = Partida.objects.all()
        return context

class EditConceptoDisplay(TemplateView):
    template_name  = 'editar/Editar-concepto.html'
    def get_context_data(self, **kwargs):
        print("get context")
        context = super(HomeView,self).get_context_data(**kwargs)
        context['conceptos'] = Concepto.objects.all()
        return context

class EditUnidadDisplay(TemplateView):
    template_name  = 'editar/Editar-unidad.html'
    def get_context_data(self, **kwargs):
        print("get context")
        context = super(HomeView,self).get_context_data(**kwargs)
        context['unidades'] = Unidad.objects.all()
        return context

"""
    Serializers
"""
class ProyectosViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer


class PartidasViewSet(viewsets.ModelViewSet):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer
