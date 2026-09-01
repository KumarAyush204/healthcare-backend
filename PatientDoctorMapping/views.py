from rest_framework.views import APIView,Response
from .models import PatientDoctorMap
from patients.models import Patient
from doctors.models import Doctor
from .serializers import PatientDoctorMappingSerialize
from doctors.serializers import DoctorSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class PatientDoctorMappingView(APIView):
    
    permission_classes=[IsAuthenticated]
    def get(self,request):
        patientdoctor=PatientDoctorMap.objects.all()
        patientdoctorData=PatientDoctorMappingSerialize(patientdoctor,many=True)
        return Response(patientdoctorData.data,status=status.HTTP_200_OK)

    def post(self,request):
        patientdoctorData=PatientDoctorMappingSerialize(data=request.data)
        if patientdoctorData.is_valid():
            patientdoctorData.save()
            return Response(patientdoctorData.data,status=status.HTTP_201_CREATED)
        return Response(patientdoctorData.errors,status=status.HTTP_400_BAD_REQUEST)    
    
    def delete(self,request,id):
        patientdoctor=get_object_or_404(PatientDoctorMap,id=id)
        patientdoctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

class PatientDoctorView(APIView):
    
    permission_classes=[IsAuthenticated]
    def get(self,request,patient_id):
        patient=get_object_or_404(Patient,id=patient_id)
        mappings=PatientDoctorMap.objects.filter(patient=patient)
        doctors=[mapping.doctor for mapping in mappings]
        doctorData=DoctorSerializer(doctors,many=True)
        return Response(doctorData.data,status=status.HTTP_200_OK)
        
