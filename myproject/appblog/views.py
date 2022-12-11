from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from appblog.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseForbidden



from myproject.settings import BASE_DIR

def about(request):
   return render(request, "appblog/about.html")


class PostList(ListView):
    model = Post
    template_name = 'appblog/inicio.html'

class PostDetail(DetailView):
   model = Post
   template_name = 'appblog/detail_post.html'

class PostCreate( CreateView):
    #permission_required = 'appblog.add_Post'
    model = Post
    success_url = ""
    fields = "__all__"
    template_name = "appblog/Post_form.html"


class PostUpdate( UpdateView):
    #permission_required = 'appblog.change_Post'
    model = Post
    success_url = ""
    fields = "__all__"

class PostDelate( DeleteView):
    #permission_required = 'appblog.delete_Post'
    model = Post
    template_name = "appblog/Post_confirm_delete.html"
    success_url = reverse_lazy("inicio")
   
