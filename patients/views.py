from patients import serializers
from rest_framework.views import APIView,Response
from .models import Patient
from .serializers import PatientSerializer
from rest_framework import status
# Create your views here.
class PatientManagement(APIView):
    def get(self,request,id=None):
        if id==None:
            patients=Patient.objects.all()
            patientsData=PatientSerializer(patients,many=True)
            return Response(patientsData.data,status=status.HTTP_200_OK)
        patient=Patient.objects.get(id=id)
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
                status=status.HTTP_400_BAD_REQUEST
        )  
    
    def delete(self,request,id):
        patient=Patient.objects.get(id=id)
        patient.delete()
        return Response({"message":"Delete Patient"})
    
    def put(self,request,id):
        patient=Patient.objects.get(id=id)
        patientData=PatientSerializer(patient,data=request.data)
        if patientData.is_valid():
            patient=patientData.save()
            return Response(PatientSerializer(patient).data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)