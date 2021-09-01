from django.shortcuts import render
from rest_framework import generics
from blog import serializers
from django.contrib.auth.models import User
from blog.models import *
from blog.permissions import *
from rest_framework import permissions
# Create your views here.

class UserListView(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=serializers.UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=serializers.UserSerializer

class BlogListView(generics.ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=serializers.BlogSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=serializers.BlogSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class CommentListView(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=serializers.CommentSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(creator=self.request.user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=serializers.CommentSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]