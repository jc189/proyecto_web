from django.urls import path
from . import views

urlpatterns = [
	path('transparencia',views.transparencia,name='transparencia'),
	path('transparencia/aviso_privacidad',views.aviso_privacidad,name='aviso_privacidad'),
	path('transparencia/conac',views.conac,name='conac'),
	path('transparencia/cuenta_publica',views.cuenta_publica,name='cuenta_publica'),
	path('transparencia/gaceta',views.gaceta,name='gaceta'),
	path('transparencia/mejora',views.mejora,name='mejora'),
	path('transparencia/pada',views.pada,name='pada'),
	path('transparencia/planeacion',views.planeacion,name='planeacion'),
	path('transparencia/sevac',views.sevac,name='sevac'),
	]