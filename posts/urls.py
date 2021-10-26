from django.urls import path
from django.urls.resolvers import URLPattern
from .import views

urlpatterns= [
    path ('', views.index, name='index'),
    path ('delete/<int:post_id>/', views.delete , name ='index'),
    path ('edit/<int:post_id>/', views.edit , name ='edit'),
    path ('like/<int:post_id>/', views.LikeView, name='like_post'),
]
 
