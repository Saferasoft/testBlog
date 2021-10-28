from .serializers import *
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response


class UsersView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class AuthUserView(APIView):
    def get(self, request):
        user = request.user
        response = UserSerializer(user)
        return Response(response.data)
