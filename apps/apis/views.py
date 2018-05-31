from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import UserSerializer, BlogSerializer, Blog_UserSerializer
from apps.blogs.models import Blog


class UserApiView(APIView):
    # Lista de usuarios
    def get(self, request):
        usr = self.request.user
        usuarios = UserSerializer(usr).data

        return Response(usuarios)


class UserDetailApiView(APIView):
    # Detalle de usuario
    def get(self, request, pk):
        queryset = User.objects.get(pk=pk)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)


class BlogApiListView(ListCreateAPIView):
    # Lista de blogs por usuario y creacion de blogs
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('usuario',)


class BlogApiDetailView(RetrieveAPIView):
    # Detalle de blog
    queryset = Blog.objects.all()
    serializer_class = Blog_UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)
