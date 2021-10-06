from rest_framework import status
from rest_framework.decorators import api_view
from .models import Nco
from .serializers import NcoSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 


@api_view(['GET', 'POST', 'DELETE'])
def nco(request):
    if request.method == 'GET':
        nco = Nco.objects.all()
        
        username = request.GET.get('username', None)
        if username is not None:
            nco = nco.filter(title__icontains=username)
        
        nco_serializer = NcoSerializer(nco, many=True)
        return JsonResponse(nco_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        nco_data = JSONParser().parse(request)
        nco_serializer = NcoSerializer(data=nco_data)
        if nco_serializer.is_valid():
            nco_serializer.save()
            return JsonResponse(nco_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(nco_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count =Nco.objects.all().delete()
        return JsonResponse({'message': '{} Nco was deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
