from django.core.management.base import BaseCommand
from employees.models import Employee
from department.models import Department
from attendance.models import Attendance
from performance.models import Performance
from faker import Faker
import random
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = "Seed the database with fake employees, departments, attendance, and performance data."

    def handle(self, *args, **kwargs):
        Performance.objects.all().delete()
        Attendance.objects.all().delete()
        Employee.objects.all().delete()
        Department.objects.all().delete()
        fake = Faker()
        self.stdout.write("Seeding data...")

        # Create Departments
        departments = []
        for name in ['HR', 'Engineering', 'Marketing', 'Sales', 'Finance']:
            dept, _ = Department.objects.get_or_create(name=name)
            departments.append(dept)

        # Create Employees
        employees = []
        for _ in range(50):
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-3y', end_date='today'),
                department=random.choice(departments)
            )
            employees.append(emp)

        # Create Attendance Records
        for emp in employees:
            for i in range(10):  # Last 10 days
                Attendance.objects.create(
                    employee=emp,
                    date=timezone.now().date() - timedelta(days=i),
                    status=random.choice(['Present', 'Absent', 'Late'])
                )

        # Create Performance Records
        for emp in employees:
            for _ in range(3):  # 3 reviews per employee
                Performance.objects.create(
                    employee=emp,
                    rating=random.randint(1, 5),
                    review_date=fake.date_between(start_date='-1y', end_date='today')
                )

        self.stdout.write(self.style.SUCCESS("Seeding complete."))
