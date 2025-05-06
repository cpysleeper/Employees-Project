"""
URL configuration for employee_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.http import JsonResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path

urlpatterns = [
    path('', lambda request: JsonResponse({'message': 'Welcome to the Employee Management API'})),
    path('admin/', admin.site.urls),
    path('api/employees/', include('employees.urls')),
    path('api/department/', include('department.urls')),
    path('api/attendance/', include('attendance.urls')),
    path('api/performance/', include('performance.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('dashboard/', include('charts.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Employee Management API",
        default_version='v1',
        description="Interactive documentation for all API endpoints",
    ),
    public=True,
    permission_classes=[],
)

urlpatterns += [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]