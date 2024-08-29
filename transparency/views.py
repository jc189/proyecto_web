from django.shortcuts import render

# Create your views here.
def transparencia(request):
	return render(request,'transparencia.html',{})

def aviso_privacidad(request):
	return render(request,'aviso_privacidad.html',{})

def conac(request):
	return render(request,'conac.html',{})

def cuenta_publica(request):
	return render(request,'cuenta_publica.html',{})

def gaceta(request):
	return render(request,'gaceta.html',{})

def mejora(request):
	return render(request,'mejora.html',{})

def pada(request):
	return render(request,'pada.html',{})

def planeacion(request):
	return render(request,'planeacion.html',{})

def sevac(request):
	return render(request,'sevac.html',{})