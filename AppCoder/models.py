from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    duracion = models.IntegerField(default=0)

    def __str__(self):
        txt="{0} - {1}"
        return txt.format(self.camada, self.nombre)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(default="")

    def __str__(self):
        txt="{0} , {1}"
        return txt.format(self.apellido, self.nombre)

class Profesor(models.Model):

    def __str__(self): # Permite mostrar la info mejor en el admin de la app
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Profesion: {self.profesion}"

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "profesores"

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEngrega = models.DateField()
    entregado = models.BooleanField()

class Certificaciones(models.Model):
    nombre = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    fecha = models.DateField()

    class Meta:
        verbose_name = "Certificaciones"
        verbose_name_plural = "Certificaciones"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatares', null = True, blank = True)

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"
