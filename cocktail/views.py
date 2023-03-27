from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from cocktail.models import Cocktail
from cocktail.serializers import CocktailSerializer


class CocktailList(generics.ListCreateAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['^drink', 'category', 'Ingredient1']
    filterset_fields = {
        'alcoholic': ['exact'],
        'category': ['exact'],
        'glass': ['exact'],
    }


class CocktailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer