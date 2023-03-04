from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor, Estudiante, Entregable
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario

# Create your views here.

def inicio(request) :
    return render(request, 'AppCoder/inicio.html')
    #return HttpResponse("vista inicio")
"""
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
"""
def cursos(request) :
    if request.method == 'POST' :
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid :
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()
            return render(request, "AppCoder/inicio.html")
        
    else :
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})

def profesores(request) :
    if request.method == 'POST' :
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid :
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()
            return render(request, "AppCoder/inicio.html")
    
    else :
        miFormulario = ProfesorFormulario()

    return render(request, "AppCoder/profesorFormulario.html", {"miFormulario":miFormulario})

def estudiantes(request) :
    if request.method == 'POST' :
        miFormulario = EstudianteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid :
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            estudiante.save()
            return render(request, "AppCoder/inicio.html")
    
    else :
        miFormulario = EstudianteFormulario()

    return render(request, "AppCoder/estudianteFormulario.html", {"miFormulario":miFormulario})

def entregables(request) :
    if request.method == 'POST' :
        miFormulario = EntregableFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid :
            informacion = miFormulario.cleaned_data
            entrega = Entregable(nombre=informacion['nombre'],apellido=informacion['apellido'] , fecha_entrega=informacion['fecha_entrega'], entregado=informacion['entregado'])
            entrega.save()
            return render(request, "AppCoder/inicio.html")
    
    else :
        miFormulario = EntregableFormulario()

    return render(request, "AppCoder/entregableFormulario.html", {"miFormulario":miFormulario})

def busquedaCamada(request) :
    return render(request, "../templates/AppCoder/busquedaCamada.html")

def buscar(request) :
    """
    mensaje = "Se busco la comisión/camada número: " + str(request.GET['camada'])
    return HttpResponse(mensaje)
    """
    if request.GET['camada'] :
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultadosPorBusqueda.html", {"cursos":cursos, "camada":camada})
    
    else :
        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)