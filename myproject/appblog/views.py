from django.shortcuts import render
from django.views.generic import ListView, DetailView
from appblog.models import Post
# Create your views here.
"""
def inicio(request):
   return render(request, "appblog/inicio.html")
   """

class inicio(ListView):
    model = Post
    template_name = 'appblog/inicio.html'