from django.urls import path 
from .views import PatientManagement

urlpatterns = [
    path('patients/', PatientManagement.as_view()),
    path('patients/<int:id>/',PatientManagement.as_view())
]