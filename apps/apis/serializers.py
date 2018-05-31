from rest_framework import serializers

from django.contrib.auth.models import User

from apps.blogs.models import Blog

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['pk',
            'password',
            'username',
            'first_name',
            'last_name',
            'email']


class Blog_UserSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(many=False)
    class Meta:
        model = Blog
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['usuario',
            'titulo',
            'contenido']
