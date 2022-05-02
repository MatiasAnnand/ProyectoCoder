from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import CursoFormulario, ProfesorFormulario
from AppCoder.models import Curso, Profesor

# Create your views here.


def curso(request):

    if request.method == 'POST':

        # info recibida del formulario html
        miFormulario = CursoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():  # comprobar si la info es valida para Django

            informacion = miFormulario.cleaned_data

            # creando un curso (del modelo) usando la info recibida
            curso = Curso(
                nombre=informacion['curso'], camada=informacion['camada'], duracion=informacion['duracion'])

            curso.save()

            # una vez guardado mostramos la plantilla de inicio
            return render(request, "AppCoder/inicio.html")

    else:
        miFormulario = CursoFormulario()  # muestra un formulario vacio

    return render(request, "AppCoder/curso.html", {"miFormulario": miFormulario})


def estudiante(request):

    return render(request, "AppCoder/estudiante.html")


def entregable(request):

    return render(request, "AppCoder/entregable.html")


def profesor(request):

    if request.method == 'POST':

        # info recibida del formulario html
        miFormulario = ProfesorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():  # comprobar si la info es valida para Django

            info = miFormulario.cleaned_data

            # creando un curso (del modelo) usando la info recibida
            profe = Profesor(nombre=info['nombre'], apellido=info['apellido'],
                             email=info['email'], profesion=info['profesion'])

            profe.save()

            # una vez guardado mostramos la plantilla de inicio
            return render(request, "AppCoder/inicio.html")

    else:
        miFormulario = ProfesorFormulario()  # muestra un formulario vacio

    dict1 = {'myForm': miFormulario}

    return render(request, "AppCoder/profesor.html", dict1)


def inicio(request):

    return render(request, "AppCoder/inicio.html")


def cursoFormulario(request):
    return


def busquedaCamada(request):

    return render(request, "AppCoder/busquedaCamada.html")


def buscar(request):

    if request.GET["camada"]:

        #respuesta=f"Estoy buscando la camada {request.GET['camada']}"
        camada = request.GET['camada']
        # cursos = Curso.objects.filter(camada__icontains=camada) #icontains significa que el numero que buscamos esta contenido en la camada
        cursos = Curso.objects.filter(camada__iexact=camada)

        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos, "camada": camada})

    else:
        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)


def listaProfesores(request):

    # almacenamos todos los profesores registrados en la base de datos
    profesores = Profesor.objects.all()

    contexto = {"profesores": profesores}

    return render(request, "AppCoder/leerProfesores.html", contexto)


def borrarProfesores(request, profesor_nombre):

    profesor = Profesor.objects.get(nombre=profesor_nombre)

    profesor.delete()

    profesores = Profesor.objects.all()

    contexto = {"profesores": profesores}

    return render(request, "AppCoder/leerProfesores.html", contexto)


def editarProfesores(request, profesor_nombre):

    profesor = Profesor.objects.get(nombre=profesor_nombre)

    if request.method == "POST":

        miFormulario = ProfesorFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']

            profesor.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = ProfesorFormulario(initial={
                                          'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email': profesor.email, 'profesion': profesor.profesion})

    return render(request, "AppCoder/editarProfesor.html", {'miFormulario': miFormulario, 'profesor_nombre': profesor_nombre})
