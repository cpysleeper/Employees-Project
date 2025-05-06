from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Performance
from .serializers import PerformanceSerializer

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['score', 'date', 'employee']  # Update with real fields
    ordering = ['-date']