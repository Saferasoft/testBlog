from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PostView, name='post list'),
    path('newPost/', AddPost, name='add post'),
    path('posts/<int:pk>',  PostDetailsView.as_view()),
    path('posts/<int:pk>/like', addLike, name='like'),
    path('likes/counter/<int:pk>', getLikes, name='like counter'),

]
