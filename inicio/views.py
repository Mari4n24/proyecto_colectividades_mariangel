from django.shortcuts import render
from inicio.models import Colectividad

def inicio(request):
    return render(request, 'inicio.html')

def crear_colectividad(request, nombre, pais):
    
    colectividades = Colectividad(nombre=nombre, pais=pais)
    colectividades.save()
    
    return render(request, 'crear_colectividad.html', {'colectividad_guardada': colectividades})

def listar_colectividades(request):
    
    cant_colectividades = Colectividad.objects.all()
    
    return render(request, 'listar_colectividades.html' , {'listado_de_colectividades': cant_colectividades})