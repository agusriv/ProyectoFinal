from django.urls import path
from appblog.views import inicio


urlpatterns = [
    path('', inicio.as_view(), name="inicio"),
]