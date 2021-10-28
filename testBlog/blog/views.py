from django.shortcuts import Http404
from .serializers import *
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def PostView(request):
    if request.method == 'GET':
        posts = Post.objects.all().order_by('date_created')
        posts_serializer = PostSerializer(posts, many=True)
        return JsonResponse(posts_serializer.data, safe=False)


@api_view(['POST'])
def AddPost(request):
    if request.method == 'POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def PostDetailsView(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return JsonResponse({'message': 'The post does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        post_serializer = PostSerializer(post)
        return JsonResponse(post_serializer.data)

    elif request.method == 'PUT':
        if request.user == post.author:
            post_data = JSONParser().parse(request)
            post_serializer = PostSerializer(post, data=post_data)
            if post_serializer.is_valid():
                post_serializer.save()
                return JsonResponse(post_serializer.data)
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        if request.user == post.author:
            post.delete()
            return JsonResponse({'message': 'Post was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        post_serializer = PostSerializer(post)
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getLikes(request, pk):
    if request.method == 'GET':
        post = Post.objects.filter(pk=pk)
        like_count = Like.objects.filter(post=post).count()
        serializer = LikeSerializer(like_count, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def addLike(request, pk):
    if request.method == 'POST':
        author = request.user
        post = Post.objects.filter(pk=pk)
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author, post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
