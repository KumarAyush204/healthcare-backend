from django.urls import path
from .views import PatientDoctorMappingView, PatientDoctorView

urlpatterns = [
    path("mappings/", PatientDoctorMappingView.as_view()),
    path("mappings/<int:id>/",PatientDoctorMappingView.as_view()),
    path(
        "mappings/<int:patient_id>",
        PatientDoctorView.as_view()
    ),
]  