from django.db import models
from patients.models import Patient
from doctors.models import Doctor

# Create your models here.
class PatientDoctorMap(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    createdAt=models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints=[models.UniqueConstraint(fields=['patient','doctor'],name='unique_patient_doctor_mapping')]
