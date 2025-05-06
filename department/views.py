from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Department
from .serializers import DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'created_at']  # Add your model fields here
    ordering = ['name']  # Optional default