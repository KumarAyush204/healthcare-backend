from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer

class UserManagement(APIView):
    def post(self,request):
        user=UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data,status=status.HTTP_200_OK)
        return Response(user.errors,status=status.HTTP_400_BAD_REQUEST)
    
