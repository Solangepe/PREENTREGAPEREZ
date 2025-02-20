from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('post/<int:post_id>/', views.ver_post, name='ver_post'),
    path('crear/', views.crear_post, name='crear_post'),
    path('buscar/', views.buscar_posts, name='buscar_posts'),
]
