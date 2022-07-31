from django import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template, loader
from Familiares.models import Pariente
# Create your views here.
def pariente(self, nombre, parentesco, edad, fecha_de_nacimiento):
    pariente=Pariente(nombre=nombre,parentesco=parentesco,edad=edad,fecha_de_nacimiento=fecha_de_nacimiento)
    pariente.save()
    return HttpResponse(f"""
    <p>{pariente.nombre} es mi {pariente.parentesco}, tiene {pariente.edad} años ya que nació en {pariente.fecha_de_nacimiento}
    </p>
    """)

def miembros_familia(self):
    lista_familiares = Pariente.objects.all()
    return render(self, "familia.html", {"miembros_familia":lista_familiares})


def inicio(self):
    return render(self, "Inicio.html")
    
def estudiantes(self):
    return render (self, 'estudiantes.html')
    
def profesores(self):
    return render (self, 'profesores.html')
    
def cursos(self):
    return render (self, 'cursos.html')
    
def entregables(self):
    return render (self, 'entregables.html')
          