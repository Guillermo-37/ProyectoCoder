from django import forms

class CursoFormulario(forms.Form) :
    # Especificar los campos.
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form) :
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class EstudianteFormulario(forms.Form) :
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class EntregableFormulario(forms.Form) :
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    fecha_entrega = forms.DateField(widget=forms.SelectDateWidget(years=range(2015, 2031)))
    entregado = forms.BooleanField()