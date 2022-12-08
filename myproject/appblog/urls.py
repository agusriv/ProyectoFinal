from django.urls import path
from appblog.views import PostList, PostDetail, PostCreate, PostUpdate


urlpatterns = [
    path('', PostList.as_view(), name="inicio"),
    path('post/<pk>/', PostDetail.as_view(), name="detalle-post"),
    path('add_post/', PostCreate.as_view(), name="agregar-post"),
    path('editar/post/<pk>',PostUpdate.as_view(), name="actualizar-post" ),
]