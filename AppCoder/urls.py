from django.urls import path
from AppCoder import views



urlpatterns = [
    
    path('cursos/', views.curso, name='Cursos'),
    path('estudiantes/', views.estudiante, name='Estudiantes'),
    path('entregables/', views.entregable, name='Entregables'),
    path('profesores/', views.profesor, name='Profesores'),
    path('', views.inicio, name='Inicio'),
    #path("cursoFormulario/", views.cursoFormulario, name='CursoFormulario'),
    path("busquedaCamada/", views.busquedaCamada, name="BusquedaCamada"),
    path("buscar/", views.buscar),
    path("listaProfes/", views.listaProfesores, name="ListaProfesores"),
    path("chauProfe/<profesor_nombre>", views.borrarProfesores, name="BorrarProfesor"),
    path("editarProfesor/<profesor_nombre>", views.editarProfesores, name="EditarProfesor"),
]