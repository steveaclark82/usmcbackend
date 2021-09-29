from rest_framework.decorators import api_view, permission_classes
from .utilities.data_access import get_pft_score
from django.http import JsonResponse
from rest_framework.permissions import AllowAny

error_message = {"error": "Unable to process your score data. Please verify your inputs and try again. If the error persists please contact "}

@api_view(['POST'])
@permission_classes([AllowAny])
def pft(request):
    request_body = request.get_json()
    score = None
    try:
        score = get_pft_score(request_body)
    except:
        return JsonResponse({"score": error_message}), 500
    return JsonResponse({"score" : score}), 200