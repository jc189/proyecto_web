from django.shortcuts import render

# Create your views here.

def about(request):
	return render(request,'about.html')

def titular(request):
	return render(request,'titular.html',{})

def directorio(request):
	return render(request,'directorio.html',{})

def mision_vision(request):
	return render(request,'mision_vision.html',{})

def valores(request):
	return render(request,'valores.html',{})

def marco(request):
	return render(request,'marco.html',{})
