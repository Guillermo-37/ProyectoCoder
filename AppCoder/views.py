from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor, Estudiante
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario

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
            curso = Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()
            return render(request, "AppCoder/inicio.html")
        
    else :
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})

def busquedaCamada(request) :
    return render(request, "../templates/AppCoder/busquedaCamada.html")

def buscar(request) :
    mensaje = "Se busco la comisión/camada número: " + str(request.GET['camada'])
    return HttpResponse(mensaje)

def profesorFormulario(request) :
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

def estudianteFormulario(request) :
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