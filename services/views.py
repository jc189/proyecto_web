from django.shortcuts import render

# Create your views here.
def servicios(request):
	return render(request,'servicios.html')

def quejas_sugerencias(request):
	return render(request,'quejas_sugerencias.html',{})

def reporte_alcantarillado(request):
	return render(request,'reporte_alcantarillado.html',{})

def reporte_fugas(request):
	return render(request,'reporte_fugas.html',{})

def requisitos(request):
	return render(request,'requisitos.html',{})

def solicitud_pipas(request):
	return render(request,'solicitud_pipas.html',{})