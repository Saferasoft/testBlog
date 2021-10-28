from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PostView, name='post list'),
    path('newPost/', AddPost, name='add post'),
    path('posts/<int:pk>',  PostDetailsView, name='post'),
    path('posts/<int:pk>/like', addLike, name='like'),
    path('post/<int:pk>/likeCounter', getLikes, name='like counter'),

]
