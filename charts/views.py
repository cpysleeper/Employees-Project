from django.shortcuts import render
from django.shortcuts import render
from employees.models import Employee
from attendance.models import Attendance
from department.models import Department
from django.db.models import Count
from django.db.models.functions import TruncMonth

def dashboard_view(request):
    # Employees per Department
    dept_data = (
        Department.objects
        .annotate(count=Count('employee'))
        .values_list('name', 'count')
    )
    dept_labels = [name for name, _ in dept_data]
    dept_counts = [count for _, count in dept_data]

    # Monthly Attendance Overview
    attendance_data = (
        Attendance.objects
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(present_count=Count('id'))
        .order_by('month')
    )
    months = [entry['month'].strftime('%B') for entry in attendance_data]
    present_counts = [entry['present_count'] for entry in attendance_data]

    return render(request, 'charts/dashboard.html', {
        'dept_labels': dept_labels,
        'dept_counts': dept_counts,
        'months': months,
        'present_counts': present_counts,
    })


