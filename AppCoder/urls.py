from django.urls import path
from AppCoder import views



urlpatterns = [
    
    path('cursos/', views.curso, name='Cursos'),
    path('estudiantes/', views.estudiante, name='Estudiantes'),
    path('entregables/', views.entregable, name='Entregables'),
    path('profesor/', views.profesor, name='Profesores'),
    path('', views.inicio, name='Inicio'),
    #path("cursoFormulario/", views.cursoFormulario, name='CursoFormulario'),
    path("busquedaCamada/", views.busquedaCamada, name="BusquedaCamada"),
    path("buscar/", views.buscar),
    path("listaProfes/", views.listaProfesores, name="ListaProfesores"),
    path("chauProfe/<profesor_nombre>", views.borrarProfesores, name="BorrarProfesor"),
    path("editarProfesor/<profesor_nombre>", views.editarProfesores, name="EditarProfesor"),

    path("curso/lista", views.CursoList.as_view(), name='ListCursos'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),

    path('login', views.login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
]