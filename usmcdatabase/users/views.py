from rest_framework import status
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

@api_view(['POST', 'GET', 'DELETE'])
def user(request):
    if request.method == 'GET':
        user = User.objects.all()
        
        username = request.GET.get('username', None)
        if username is not None:
            user = user.filter(title__icontains=username)
        
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
# Create your views here.
