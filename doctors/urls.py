from django.urls import path 
from .views import DoctorManagement

urlpatterns = [
    path('doctors/', DoctorManagement.as_view()),
    path('doctors/<int:id>/',DoctorManagement.as_view())
]