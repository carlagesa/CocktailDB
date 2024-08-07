from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
import random

class DrinkListView(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = [permissions.IsAuthenticated]

class DrinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = [permissions.IsAuthenticated]

class DrinkSearchByNameView(generics.ListAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

@api_view(['GET'])
def search_by_ingredient(request):
    ingredient = request.GET.get('ingredient')
    if not ingredient:
        return Response({'detail': 'Ingredient parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
    drinks = Drink.objects.filter(ingredients__icontains=ingredient)
    serializer = DrinkSerializer(drinks, many=True)
    return Response(serializer.data)

class DrinkFilterView(APIView):
    def get(self, request, *args, **kwargs):
        category = request.query_params.get('category')
        glass = request.query_params.get('glass')
        alcoholic = request.query_params.get('alcoholic')

        filters = {}
        if category:
            filters['category'] = category
        if glass:
            filters['glass'] = glass
        if alcoholic:
            filters['alcoholic'] = alcoholic

        drinks = Drink.objects.filter(**filters)
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)
import logging

logger = logging.getLogger(__name__)

class RandomDrinkView(APIView):
    def get(self, request, *args, **kwargs):
        count = Drink.objects.count()
        if count == 0:
            logger.debug("No drinks available in the database.")
            return Response({'detail': 'No drinks available'}, status=status.HTTP_404_NOT_FOUND)
        
        random_index = random.randint(0, count - 1)
        logger.debug(f"Random index generated: {random_index}")
        
        try:
            drink = Drink.objects.all()[random_index]
            serializer = DrinkSerializer(drink)
            return Response(serializer.data)
        except Drink.DoesNotExist:
            logger.error("Drink not found even though count was non-zero.")
            return Response({'detail': 'No drinks available'}, status=status.HTTP_404_NOT_FOUND)
        except IndexError:
            logger.error("IndexError: Random index out of range.")
            return Response({'detail': 'Random index out of range'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class LatestDrinksView(generics.ListAPIView):
    queryset = Drink.objects.order_by('-id')[:10]
    serializer_class = DrinkSerializer
