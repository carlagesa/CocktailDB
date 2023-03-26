from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from cocktail.models import Cocktail
from cocktail.serializers import CocktailSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class CocktailList(generics.ListCreateAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['drink', 'category', 'Ingredient1']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'alcoholic': ['exact'],
        'category': ['exact'],
        'glass': ['exact'],
    }

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="cocktail",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Search by name of the cocktail",
            ),
            openapi.Parameter(
                name="glass",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Search by type of glass",
            ),
            openapi.Parameter(
                name="drink",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Search by type of drink",
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CocktailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer