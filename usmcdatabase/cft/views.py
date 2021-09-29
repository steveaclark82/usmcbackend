from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .utilities.data_access import get_cft_score
from django.http import JsonResponse

error_message = {"error": "Unable to process your score data. Please verify your inputs and try again. If the error persists please contact "}

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def usmc_pft(request):
    request_body = request.get_json()
    score = None
    try:
        score = get_cft_score(request_body)
    except:
        return JsonResponse({"score": error_message}), 500
    return JsonResponse({"score" : score}), 200