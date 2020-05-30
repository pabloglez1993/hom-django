from rest_framework.serializers import ModelSerializer
from HogaresYObrasMexicanas.models import Direccion,Proyecto,Partida

class DireccionSerializer(ModelSerializer):
    class Meta:
        model = Direccion
        fields = ("id","calle","numero","colonia","municipio","estado","codigo_postal")

class ProyectoSerializer(ModelSerializer):
    direccion = DireccionSerializer() 
    class Meta:
        model = Proyecto
        fields = ("id","titulo","propietario","presupuesto","direccion")

class PartidaSerializer(ModelSerializer):
    class Meta:
        model = Partida
        fields = ("nombre","proyecto")
