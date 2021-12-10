from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Post 
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework import generics, permissions
# Create your views here.

class PostList(generics.ListCreateAPIView):
	#permission_classes = (permissions.IsAuthenticated,)
	queryset = Post.objects.all()
	serializer_class= PostSerializer  


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthorOrReadOnly,)
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
