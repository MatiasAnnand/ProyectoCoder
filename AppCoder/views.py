from dataclasses import fields
from msilib.schema import ListView
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import CursoFormulario, ProfesorFormulario, RegistroFormulario
from AppCoder.models import Avatar, Curso, Estudiante, Profesor
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate



# Vista para registrarse
def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user=form.cleaned_data['username']
            form.save()

            return render(request, "AppCoder/inicio.html", {'mensaje':"Usuario Creado"})

    else:

        form = UserCreationForm()  # formulario de django que permite crear usuarios

    return render(request, "AppCoder/registro.html", {'form':form})


# Vista para iniciar sesion
def login_request(request):
    
    if request.method == 'POST':  # al presionar el boton "Iniciar Sesion"

        form = AuthenticationForm(request, data = request.POST)  # leer la data del formulario de inicio de sesion

        if form.is_valid():

            usuario=form.cleaned_data.get('username')  # leer el usuario ingresado. Username y password son default de Django
            contra=form.cleaned_data.get('password')  # leer la contraseña ingresada

            user=authenticate(username=usuario, password=contra)  # busca al usuario con los datos ingresados

            if user:  # si ha enconrado un usuario con esos datos

                login(request, user)  # hacemos login

                return render(request, "AppCoder/inicio.html", {'mensaje':f"Bienvenido {user}"})  # mensaje de bienvenida en la pagina de inicio

        else:

            form = AuthenticationForm()  # muestra el formulario

        return render(request, "AppCoder/login.html", {'form':form})  # vincular la vista con la plantilla del html


# Pagina Principal
@login_required
def inicio(request):

    avatares = Avatar.objects.filter(user=request.user.id)
    imagen = avatares[0].imagen.url
    return render(request, "AppCoder/inicio.html", {'url':imagen})


 # Vista para crear Cursos
@login_required
def agregarCurso(request):

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


 # Agregar Estudiante
def agregarEstudiante(request):

    return render(request, "AppCoder/estudiante.html")

 # Agregar Entregables
def agregarEntregable(request):

    return render(request, "AppCoder/entregable.html")

 # Agregar Profesores
def agregarProfesor(request):

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



@login_required
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

@login_required
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


def editarUsuario(request):

    usuario = request.user

    if request.method == "POST":

        miFormulario = RegistroFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.username = informacion['nombre']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = RegistroFormulario(initial={'username': usuario.nombre, 'email': usuario.email})

    return render(request, "AppCoder/editarUsuario.html", {'miFormulario': miFormulario, 'usuario': usuario.username})


@login_required
def listaProfesores(request):

    # almacenamos todos los profesores registrados en la base de datos
    profesores = Profesor.objects.all()

    contexto = {"profesores": profesores}

    return render(request, "AppCoder/leerProfesores.html", contexto)

def about(request):
    return render(request, 'AppCoder/about.html')

# Vista para mostrar a los cursos usando Clases.
class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'AppCoder/listaCursos.html'

# Vista para mostrar el detalle de los cursos usando Clases (CRUD con Clases)
class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppCoder/cursoDetalle.html"

# Vista para crear cursos usando Clases (CRUD con Clases)
class CursoCreacion(CreateView):
    model = Curso
    success_url = "/AppCoder/curso/lista"
    fields = ['nombre', 'camada', 'duracion']

# Vista para mostrar/ actualizar los cursos usando Clases (CRUD con Clases)
class CursoUpdate(UpdateView):
    model = Curso
    success_url = "/AppCoder/curso/lista"
    fields = ['nombre', 'camada', 'duracion']

class CursoDelete(DeleteView):
    model = Curso
    success_url = "/AppCoder/curso/lista"

# Vista para mostrar a los estudiantes usando Clases.
class EstudianteList(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = 'AppCoder/listaEstudiante.html'