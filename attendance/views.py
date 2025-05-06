from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Attendance
from .serializers import AttendanceSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date', 'status', 'employee']  # Update as needed
    ordering = ['-date']