# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from cocktail.models import Cocktail
from cocktail.serializers import CocktailSerializer

class CocktailList(generics.ListCreateAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['drink', 'category','Ingredient1']


class CocktailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

