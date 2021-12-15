from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import *
from .serializers import PostSerializer, UserSerializer, BSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework import generics, permissions
# Create your views here.

class TrainList(generics.ListCreateAPIView):
	#permission_classes = (permissions.IsAuthenticated,)
	queryset = T.objects.all()
	serializer_class= PostSerializer

class TicketBooking(generics.ListCreateAPIView):
	queryset = B.objects.all()
	serializer_class = BSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthorOrReadOnly,)
	queryset = T.objects.all()
	serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
