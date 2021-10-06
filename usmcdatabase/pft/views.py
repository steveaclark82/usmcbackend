from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Three_Mile, Row, Crunches, Plank, Pullups, Pushups
from .serializers import Three_MileSerializer, RowSerializer, CrunchesSerializer, PlankSerializer, PullupsSerializer, PushupsSerializer



# Create your views here.
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def Three_Mile(request, id):
    if request.method == 'POST':
        serializer = Three_MileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(three_mile=request.three_mile)
            return Response(status.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        wod = Three_Mile.objects.filter(id=id)
        serializer = Three_MileSerializer(wod, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def Row(request, id):
    if request.method == 'POST':
        serializer = RowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(row=request.row)
            return Response(status.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        like = Row.objects.filter(id=id)
        serializer = RowSerializer(like, many=True)
        return Response(serializer.data)
    
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def Crunches(request, id):
    if request.method == 'POST':
        serializer = CrunchesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(crunches=request.crunches)
            return Response(status.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        like = Crunches.objects.filter(id=id)
        serializer = CrunchesSerializer(like, many=True)
        return Response(serializer.data)
    
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def Plank(request, id):
    if request.method == 'POST':
        serializer = PlankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(plank=request.plank)
            return Response(status.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        like = Plank.objects.filter(id=id)
        serializer = PlankSerializer(like, many=True)
        return Response(serializer.data)
    
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def Pullups(request, id):
    if request.method == 'POST':
        serializer = PullupsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(pullups=request.pullups)
            return Response(status.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        like = Pullups.objects.filter(id=id)
        serializer = PullupsSerializer(like, many=True)
        return Response(serializer.data)
    
@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def Pushups(request, id):
    if request.method == 'POST':
        serializer = PushupsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(pushups=request.pushups)
            return Response(status.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        like = Pushups.objects.filter(id=id)
        serializer = PushupsSerializer(like, many=True)
        return Response(serializer.data)


