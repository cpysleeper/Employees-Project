from django.shortcuts import render
from .serializers import EmployeeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Employee
from .permissions import IsAdminOrReadOnly


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'email', 'date_of_joining','department']
    ordering = ['name']  # default ordering (optional)