from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Movement_Contact, Maneuver_Fire, Ammo_Lift
from .serializers import Movement_ContactSerializer, Maneuver_FireSerializer, Ammo_LiftSerializer
from django.contrib.auth.models import User



# Create your views here.
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def Movement_Contact(request, id=1):
    if request.method == 'POST':
        serializer = Movement_ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        wod = Movement_Contact.objects.filter(id=id)
        serializer = Movement_ContactSerializer(wod, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def Maneuver_Fire(request, id=1):
    if request.method == 'POST':
        serializer = Maneuver_FireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        like = Maneuver_Fire.objects.filter(id=id)
        serializer = Maneuver_FireSerializer(like, many=True)
        return Response(serializer.data)
    
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def Ammo_Lift(request, id=1):
    if request.method == 'POST':
        serializer = Ammo_LiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        like = Ammo_Lift.objects.filter(id=id)
        serializer = Ammo_LiftSerializer(like, many=True)
        return Response(serializer.data)