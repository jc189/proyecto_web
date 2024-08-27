from django.urls import path
from . import views

urlpatterns = [
	path('about',views.about,name='about'),
	path('about/titular',views.titular,name='titular'),
	path('about/directorio',views.titular,name='directorio'),
	path('about/mision_vision',views.titular,name='mision_vision'),
	path('about/marco',views.titular,name='marco_juridico'),
	path('about/valores',views.titular,name='valores')
	]