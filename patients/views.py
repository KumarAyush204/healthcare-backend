
from rest_framework.views import APIView,Response
from .models import Patient
from .serializers import PatientSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.
class PatientManagement(APIView):
    def get(self,request,id=None):
        if id==None:
            patients=Patient.objects.all()
            patientsData=PatientSerializer(patients,many=True)
            return Response(patientsData.data,status=status.HTTP_200_OK)
        patient=get_object_or_404(Patient,id=id)
        patientData=PatientSerializer(patient)
        return Response(patientData.data,status=status.HTTP_200_OK)

    def post(self,request):
        patientData=PatientSerializer(data=request.data)

        if patientData.is_valid():
            patient=patientData.save()
            return Response(
                PatientSerializer(patient).data,
                status=status.HTTP_201_CREATED
            )
        return Response(
                patientData.errors,
                status=status.HTTP_400_BAD_REQUEST
        )  
    
    def put(self,request,id):
        patient=get_object_or_404(Patient,id=id)
        patientData=PatientSerializer(patient,data=request.data)
        if patientData.is_valid():
            patient=patientData.save()
            return Response(PatientSerializer(patient).data,status=status.HTTP_200_OK)
        return Response(patientData.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,id):
        patient=get_object_or_404(Patient,id=id)
        patientData=PatientSerializer(patient,data=request.data,partial=True)
        if patientData.is_valid():
            patient=patientData.save()
            return Response(PatientSerializer(patient).data,status=status.HTTP_200_OK)
        return Response(patientData.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        patient=get_object_or_404(Patient,id=id)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        