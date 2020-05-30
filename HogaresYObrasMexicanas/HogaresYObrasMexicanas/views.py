from django.views.generic import TemplateView
from HogaresYObrasMexicanas.models import Proyecto,Partida
from rest_framework.generics import ListCreateAPIView
from HogaresYObrasMexicanas.serializers import ProyectoSerializer,PartidaSerializer
class HomeView(TemplateView):
    template_name  = 'index.html'
    def get_context_data(self, **kwargs):
        print("get context")
        context = super(HomeView,self).get_context_data(**kwargs)
        context['proyectos']=Proyecto.objects.all()
        return context

class ProyectosListView(ListCreateAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer


class PartidasListView(ListCreateAPIView):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer
