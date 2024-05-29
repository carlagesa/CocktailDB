from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from cocktail.models import Cocktail
from cocktail.serializers import CocktailSerializer
from rest_framework.views import APIView
from django.http import HttpResponse, Http404
from django.conf import settings
from django.shortcuts import get_object_or_404
import os
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

class ImageView(APIView):
    def get(self, request, path):
        # Construct the full path to the image
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                return HttpResponse(f.read(), content_type="image/jpeg")
        else:
            raise Http404("Image not found")