from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(request):

    # Get all the drinks
    # Serialize them
    # Return JSON
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({"drinks": serializer.data}, safe=False)