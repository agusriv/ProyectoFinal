from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=60)
    titulo_tag = models.CharField(max_length=60)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} + ' | ' + str{self.autor}"
    
    def get_absolute_url(self):
        return reverse ('inicio')
