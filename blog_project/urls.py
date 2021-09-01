"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',UserListView.as_view()),
    path('users/<int:pk>/',UserDetailView.as_view()),
    path('blogs/',BlogListView.as_view()),
    path('blogs/<int:pk>',BlogDetailView.as_view()),
    path('api-auth/',include('rest_framework.urls')),
    path('comments/',CommentListView.as_view()),
    path('comments/<int:pk>',CommentDetailView.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)