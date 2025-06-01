from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Topic, Category
from .serializers import TopicSerializer, CategorySerializer

# Create your views here.

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
