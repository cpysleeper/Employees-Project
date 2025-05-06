# 🧑‍💼 Employee Management System

A Django-based API project for managing employees, departments, attendance, and performance — built with Swagger docs, PostgreSQL, and optional Chart.js visualizations. There are two types of 
default users: Admin and Employee. Admin can view and make change to all the data. Employee is only allowed to view the data. 

## 🚀 Features

- 🔁 CRUD APIs for Employees, Departments, Attendance, and Performance
- 🧾 Swagger API documentation (`/swagger/`)
- 🔐 JWT or Token Authentication-ready
- 📊 Chart.js Visualizations:
  - Employees per Department (Pie Chart)
  - Monthly Attendance Overview (Bar Chart)
- 🧪 Faker-based seed command for dummy data
- ⚙️ Modular Django app structure
- 🐘 PostgreSQL database via `.env` config

---

## 📁 Project Structure

employee_project/
├── employees/ # Employee model, views, serializers
├── attendance/ # Attendance model, views, serializers
├── performance/ # Performance model, views, serializers
├── department/ # Department model
├── charts/ # Optional visual dashboards
├── employee_project/ # Project settings
├── templates/ # Dashboard templates
├── .env.example # Sample environment variables
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```
git clone git@github.com:cpysleeper/Employees-Project.git
cd Employees-Project 
```

2. Set Up Environment
Create .env from the provided template:
```
cp .env.example .env
```
Update with your local PostgreSQL credentials.

3. Create Virtual Environment & Install Dependencies
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
4. Create the Database
Make sure PostgreSQL is running. Then create the DB:
```
psql -U postgres
CREATE DATABASE employee_db;
\q
```

5. Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```

6. Seed Fake Data
```
python manage.py seed_data  # After implementing the management command
```

7. Run the Server
```
python manage.py runserver
```

Visit:

http://localhost:8000/swagger/ — Swagger docs

http://localhost:8000/dashboard/ — Charts

http://localhost:8000/admin - User management


🧪 Technologies Used
Django 4.x

Django REST Framework

PostgreSQL

drf-yasg 

django-environ

Chart.js

Faker


📊 Example Charts
👥 Employees per Department (Pie Chart)

📅 Monthly Attendance Overview (Bar Chart)

📄 License
MIT License — use freely for learning or building!

🙌 Author
Project built by @cpysleeper as part of a Django internship challenge.



