from django.shortcuts import render
from appfinalds.models import *
from appfinalds.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request,"appfinalds/inicio.html")

def asesores(request):
    return render(request,"appfinalds/asesores.html")

def evaluadores(request):
    return render(request,"appfinalds/evaluadores.html")

def evaluaciones(request):
    return render(request,"appfinalds/evaluaciones.html")

def about(request):
    return render(request,"appfinalds/about.html")


@login_required
def agregar_asesores(request):
    if request.method == 'POST':
        miformulario = AsesoresFormulario(request.POST)
        
        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
            asesor = Asesor(nombre=informacion['nombre'],apellido=informacion['apellido'],id_asesor=informacion['id_asesor'])
            asesor.save()

            return render(request,"appfinalds/asesor_registrado.html")
    else:
        miformulario = AsesoresFormulario()
            
    return render(request,"appfinalds/agregar_asesores.html")

@login_required
def agregar_evaluadores(request):
    if request.method == 'POST':
        miformulario = EvaluadorFormulario(request.POST)
        
        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
            evaluador = Evaluador(nombre=informacion['nombre'],apellido=informacion['apellido'],id_evaluador=informacion['id_evaluador'])
            evaluador.save()

            return render(request,"appfinalds/evaluador_registrado.html")
    else:
        miformulario = EvaluadorFormulario()
            
    return render(request,"appfinalds/agregar_evaluadores.html")

@login_required
def agregar_evaluaciones(request):
    if request.method == 'POST':
        miformulario = EvaluacionFormulario(request.POST)
        
        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
            asesor = Evaluacion(id_evaluador=informacion['id_evaluador'],id_asesor=informacion['id_asesor'],id_evaluacion=informacion['id_evaluacion'],fecha_evaluacion=informacion['fecha_evaluacion'])
            asesor.save()

            return render(request,"appfinalds/evaluacion_registrada.html")
    else:
        miformulario = EvaluacionFormulario()
            
    return render(request,"appfinalds/agregar_evaluaciones.html")

@login_required
def busqueda_asesor(request):
    return render(request,"appfinalds/busqueda_asesor.html")

def find_asesores(request):
    if request.GET["id_asesor"]:
        id_asesor = request.GET["id_asesor"]
        nombres = Asesor.objects.filter(id_asesor__icontains=id_asesor)
        apellidos = Asesor.objects.filter(id_asesor__icontains=id_asesor)
        
        return render(request,"appfinalds/find_asesores.html", {"nombres":nombres,"apellidos":apellidos,"id_asesor":id_asesor})
    else:
        return render(request,"appfinalds/no_find_asesores.html")

@login_required
def busqueda_evaluador(request):
    return render(request,"appfinalds/busqueda_evaluador.html")

def find_evaluador(request):
    if request.GET["id_evaluador"]:
        id_evaluador = request.GET["id_evaluador"]
        nombres = Evaluador.objects.filter(id_evaluador__icontains=id_evaluador)
        apellidos = Evaluador.objects.filter(id_evaluador__icontains=id_evaluador)
        return render(request,"appfinalds/find_evaluadores.html", {"nombres":nombres,"apellidos":apellidos,"id_evaluador":id_evaluador})
    else:
        return render(request,"appfinalds/no_find_evaluadores.html")

@login_required
def busqueda_evaluacion(request):
    return render(request,"appfinalds/busqueda_evaluacion.html")

def find_evaluacion(request):
    if request.GET["id_evaluacion"]:
        id_evaluacion = request.GET["id_evaluacion"]
        id_evaluadores = Evaluacion.objects.filter(id_evaluacion__icontains=id_evaluacion)
        id_asesores = Evaluacion.objects.filter(id_evaluacion__icontains=id_evaluacion)
        fecha_evaluaciones = Evaluacion.objects.filter(id_evaluacion__icontains=id_evaluacion)
        return render(request,"appfinalds/find_evaluaciones.html", {"id_evaluadores":id_evaluadores,"id_asesores":id_asesores,"id_evaluacion":id_evaluacion,"fecha_evaluaciones":fecha_evaluaciones})
    else:
        return render(request,"appfinalds/no_find_evaluaciones.html")
    
