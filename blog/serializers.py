from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    blogs=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model=User
        fields=('id', 'username', 'blogs', 'comments')

class BlogSerializer(serializers.ModelSerializer):
    creator=serializers.ReadOnlyField(source='creator.username')
    comments=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model=Blog
        fields=['id', 'creator', 'title', 'description', 'comments']

class CommentSerializer(serializers.ModelSerializer):
    creator=serializers.ReadOnlyField(source='creator.username')
    class Meta:
        model=Comment
        fields=['id', 'description', 'creator', 'blog']