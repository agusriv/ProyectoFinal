from django.urls import path
from appblog.views import inicio, PostDetail


urlpatterns = [
    path('', inicio.as_view(), name="inicio"),
    path('post/<pk>/', PostDetail.as_view(), name="detalle-post"),
]