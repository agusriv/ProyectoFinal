from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=60)
    imagen_cabezera = models.ImageField(null=True, blank=True, upload_to="imagenes/")
    titulo_tag = models.CharField(max_length=60)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = RichTextField(blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=100, default='click en el link para leer mas')

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)
    
    def get_absolute_url(self):
        return reverse ('inicio')

class Perfil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    perfil_imagen = models.ImageField(null=True, blank=True, upload_to="imagenes/perfil/")
    Instagram_url = models.CharField(max_length=255, null=True, blank=True)
    github_url =  models.CharField(max_length=255, null=True, blank=True)
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    web_url =  models.CharField(max_length=255, null=True, blank=True)
    Twitter_url = models.CharField(max_length=255, null=True, blank=True)
    

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse ('inicio')

class Comment(models.Model):
    
    post = models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self) :
       return '%s - %s' % (self.post.titulo, self.name)

    


