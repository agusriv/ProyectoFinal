from django.urls import path
from appblog2.views import UserRegisterView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),

]