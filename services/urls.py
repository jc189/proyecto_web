from django.urls import path
from . import views

urlpatterns = [
	path('servicios/',views.servicios,name='servicios'),
	path('servicios/quejas_sugerencias',views.quejas_sugerencias,name='quejas_sugerencias'),
	path('servicios/reporte_alcantarillado',views.reporte_alcantarillado,name='reporte_alcantarillado'),
	path('servicios/reporte_fugas',views.reporte_fugas,name='reporte_fugas'),
	path('servicios/requisitos',views.requisitos,name='requisitos'),
	path('servicios/solicitud_pipas',views.solicitud_pipas,name='solicitud_pipas')
	]