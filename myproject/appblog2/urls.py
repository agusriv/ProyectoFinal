from django.urls import path
from appblog2.views import UserRegisterView, UserEditView, PasswordsCambiarView
from appblog2.views import password_succes


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edir_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsCambiarView.as_view(template_name='registration/change-password.html')),
    path('password_succes/', password_succes, name='password_success'),

]