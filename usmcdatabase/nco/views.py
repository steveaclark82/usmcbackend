from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Nco
from .serializers import UserSerializer
from django.contrib.auth.models import User


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_nco(request):
    users = Nco.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def get_nco(request, id):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        users = Nco.objects.filter(id=id)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

# Create your views here.


# Create your views here.
