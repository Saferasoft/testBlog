from django.shortcuts import Http404
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework import viewsets


class PostsView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class AddLikeView(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()


class PostDetailsView(APIView):
    def get_object(self, pk,  *args, **kwargs):
        try:
            return Post.objects.filter().get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request,  pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


class LikeCounterView(APIView):
    def get(self, request, pk, format=None):
        counter = 0
        likes = Like.objects.all()
        for like in likes:
            if like.post.id == pk:
                counter += 1
        print('couter' + str(counter))
        return Response(counter)


class UsersView(APIView):
    def get(self, request, username, format=None):
        user = User.objects.get(username=username)
        user = {
            'fullName': user.get_full_name()
        }
        return Response(user)
