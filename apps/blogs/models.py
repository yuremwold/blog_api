from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    fecha_registro = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField('Titulo', max_length=100)
    contenido = models.CharField('Contenido', max_length=100)

    def __str__(self):
        return "Titulo: {}, autor {}, fecha: {}".format(self.titulo, self.usuario.username, self.fecha_registro)
