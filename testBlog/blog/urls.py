from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("posts", views.PostsView, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    path('likes/counter/<int:pk>', views.LikeCounterView.as_view()),
    path('posts/<int:pk>',  views.PostDetailsView.as_view()),
    path('user/<str:username>',  views.UsersView.as_view()),
]
