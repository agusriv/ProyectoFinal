from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=60)
    titulo_tag = models.CharField(max_length=60)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = RichTextField(blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=100, default='click en el link para leer mas')

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)
    
    def get_absolute_url(self):
        return reverse ('inicio')


