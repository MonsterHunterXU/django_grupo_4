from django.contrib import admin
from django.urls import path,include
from .views import index,quienesSomos,galeria,registro,login,logout_vista,admin_insumos,eliminarInsumo,modificarInsumo,Actualizar,guardar_token,contacto

urlpatterns = [
    path('',index,name='INDEX'),
    path('Quienes_Somos/',quienesSomos,name='QUIEN'),
    path('Galeria/',galeria,name='GALE'),
    path('Registro/',registro,name='REGI'),
    path('admin_insumos/',admin_insumos,name='ADMI'),
    path('contacto/',contacto,name='CON'),
    path('login/',login,name='LOGI'),
    path('logout_vista/',logout_vista,name='LOGOUT'),
    path('eliminarinsumo/<id>/', eliminarInsumo, name='ELIMI'),
    path('modificar_Insumo/<id>/', modificarInsumo, name='MODI'),
    path('Actualizar/', Actualizar, name='ACTU'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('guardar-token/', guardar_token, name='guardar-token'),

]