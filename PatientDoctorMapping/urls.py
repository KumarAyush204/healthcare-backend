from django.urls import path
from .views import PatientDoctorMappingView, PatientDoctorView

urlpatterns = [
    path("patient-doctor-mapping/", PatientDoctorMappingView.as_view()),
    path("patient-doctor-mapping/<int:id>/",PatientDoctorMappingView.as_view()),
    path(
        "patient/<int:patient_id>/doctors/",
        PatientDoctorView.as_view()
    ),
]