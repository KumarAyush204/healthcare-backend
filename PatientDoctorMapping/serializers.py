from rest_framework import serializers
from .models import PatientDoctorMap


class PatientDoctorMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientDoctorMap
        fields = ["id", "patient", "doctor", "createdAt"]
        read_only_fields = ["id", "createdAt"]