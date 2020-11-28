from django.shortcuts import render

from LavadoAutos.models import Insumos, Contacto
from .serializer import InsumoSerealizer, ContactoSerealizer
from rest_framework import generics


# Create your views here.
class InsumosViewSet(generics.ListCreateAPIView):
    queryset = Insumos.objects.all()
    serializer_class = InsumoSerealizer

class InsumosFiltroNombreViewSet(generics.ListAPIView):
    serializer_class = InsumoSerealizer
    def get_queryset(self):
        elnombre = self.kwargs['nombre']
        return Insumos.objects.filter(nombreinsumo=elnombre)

class InsumosFiltroPrecioViewSet(generics.ListAPIView):
    serializer_class = InsumoSerealizer
    def get_queryset(self):
        elprecio = self.kwargs['precio']
        return Insumos.objects.filter(precio=elprecio)

# Contacto Api
class ContactoViewSet(generics.ListCreateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerealizer
    