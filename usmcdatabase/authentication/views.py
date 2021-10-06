from django.contrib.auth.models import User
from .serializers import RegistrationSerializer
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.permissions import  AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    
class UserView(APIView):
    
    def post(self, request, id=1):
        if request.method == 'POST':
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=1):
        users = User.objects.get(pk=id)
        serializer = RegistrationSerializer(users)
        return Response(serializer.data)

