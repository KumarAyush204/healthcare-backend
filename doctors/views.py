
from rest_framework.views import APIView,Response
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class DoctorManagement(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,id=None):
        if id==None:
            doctors=Doctor.objects.all()
            doctorsData=DoctorSerializer(doctors,many=True)
            return Response(doctorsData.data,status=status.HTTP_200_OK)
        doctor=get_object_or_404(Doctor,id=id)
        doctorData=DoctorSerializer(doctor)
        return Response(doctorData.data,status=status.HTTP_200_OK)

    def post(self,request):
        doctorData=DoctorSerializer(data=request.data)
        if doctorData.is_valid():
            doctor=doctorData.save()
            return Response(DoctorSerializer(doctor).data,status=status.HTTP_201_CREATED)
        return Response(doctorData.errors,status=status.HTTP_400_BAD_REQUEST)      
    
    def put(self,request,id):
        doctor=get_object_or_404(Doctor,id=id)
        doctorData=DoctorSerializer(doctor,data=request.data)
        if doctorData.is_valid():
            doctor=doctorData.save()
            return Response(DoctorSerializer(doctor).data,status=status.HTTP_200_OK)
        return Response(doctorData.errors,status=status.HTTP_400_BAD_REQUEST)   
    def patch(self,request,id):
        doctor=get_object_or_404(Doctor,id=id)
        doctorData=DoctorSerializer(doctor,data=request.data,partial=True)
        if doctorData.is_valid():
            doctor=doctorData.save()
            return Response(DoctorSerializer(doctor).data,status=status.HTTP_200_OK)
        return Response(doctorData.errors,status=status.HTTP_400_BAD_REQUEST)   
    
    def delete(self,request,id):
        doctor=get_object_or_404(Doctor,id=id)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
