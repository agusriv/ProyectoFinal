from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from appblog.models import Post



from myproject.settings import BASE_DIR
# Create your views here.

"""
def inicio(request):
   return render(request, "appblog/inicio.html")
   """

class PostList(ListView):
    model = Post
    template_name = 'appblog/inicio.html'

class PostDetail(DetailView):
   model = Post
   template_name = 'appblog/detail_post.html'

class PostCreate(CreateView):
    model = Post
    success_url = ""
    fields = "__all__"
    template_name = "appblog/Post_form.html"

class PostUpdate(UpdateView):
    model = Post
    success_url = ""
    fields = "__all__"
   
