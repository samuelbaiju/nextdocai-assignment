from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Project, DevelopmentTask, DesignTask
from .serializers import ProjectSerializer, DevelopmentTaskSerializer, DesignTaskSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['created_at']

class DevelopmentTaskViewSet(viewsets.ModelViewSet):
    queryset = DevelopmentTask.objects.all()
    serializer_class = DevelopmentTaskSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    filterset_fields = ['status', 'due_date']

class DesignTaskViewSet(viewsets.ModelViewSet):
    queryset = DesignTask.objects.all()
    serializer_class = DesignTaskSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    filterset_fields = ['status', 'due_date']