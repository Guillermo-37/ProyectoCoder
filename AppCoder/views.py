from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario

# Create your views here.

def inicio(request) :
    return render(request, 'AppCoder/inicio.html')
    #return HttpResponse("vista inicio")

def cursos(request) :
    return render(request, 'AppCoder/cursos.html')
    #return HttpResponse("vista cursos")

def profesores(request) :
    return render(request, 'AppCoder/profesores.html')
    #return HttpResponse("vista profesores")

def entregables(request) :
    return render(request, 'AppCoder/entregables.html')
    #return HttpResponse("vista entregables")

def estudiantes(request) :
    return render(request, 'AppCoder/estudiantes.html')
    #return HttpResponse("vista estudiantes")

def cursoFormulario(request) :
    if request.method == 'POST' :
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid :
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], comision=informacion['comision'])
            curso.save()
            return render(request, "AppCoder/inicio.html")
        
    else :
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})

def busquedaComision(request) :
    return render(request, "AppCoder/busquedaComision.html")

"""
def buscar(request) :
    respuesta = f"Estoy buscando la comision número: {request.GET['comision']}"
    return HttpResponse(respuesta)
"""

def buscar(request) :
    if request.GET["comision"] :
        comision = request.GET["comision"]
        cursos = Curso.objects.filter(comision__icontains=comision)
        return render(request, "resultadoBusqueda.html", {"cursos":cursos, "comision":comision})

    else :
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)