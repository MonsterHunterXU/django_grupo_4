from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^api/Insumos/$',views.InsumosViewSet.as_view()),
    url(r'^api/Insumos_nombre/(?P<nombre>.+)/$',views.InsumosFiltroNombreViewSet.as_view()),
    url(r'^api/Insumos_precio/(?P<precio>[0-9]+)/$',views.InsumosFiltroPrecioViewSet.as_view()),
    url(r'^api/Contacto/$',views.ContactoViewSet.as_view()),
]
