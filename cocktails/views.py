from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Cocktail, Ingredient
from .serializers import CocktailSerializer, IngredientSerializer
import random

# Cocktail Views
class CocktailOnlyListView(generics.ListAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

class SearchCocktailByName(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        cocktails = Cocktail.objects.filter(name__icontains=name)
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

class ListCocktailsByFirstLetter(APIView):
    def get(self, request):
        letter = request.query_params.get('letter')
        cocktails = Cocktail.objects.filter(name__istartswith=letter)
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

class LookupCocktailById(APIView):
    def get(self, request):
        cocktail_id = request.query_params.get('id')
        try:
            cocktail = Cocktail.objects.get(id=cocktail_id)
            serializer = CocktailSerializer(cocktail)
            return Response(serializer.data)
        except Cocktail.DoesNotExist:
            return Response({"error": "Cocktail not found"}, status=404)

class LookupRandomCocktail(APIView):
    def get(self, request):
        cocktails = Cocktail.objects.all()
        if cocktails.exists():
            cocktail = random.choice(cocktails)
            serializer = CocktailSerializer(cocktail)
            return Response(serializer.data)
        else:
            return Response({"error": "No cocktails available"}, status=404)

# Ingredient Views
class SearchIngredientByName(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        ingredients = Ingredient.objects.filter(name__icontains=name)
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

class LookupIngredientById(APIView):
    def get(self, request):
        ingredient_id = request.query_params.get('id')
        try:
            ingredient = Ingredient.objects.get(id=ingredient_id)
            serializer = IngredientSerializer(ingredient)
            return Response(serializer.data)
        except Ingredient.DoesNotExist:
            return Response({"error": "Ingredient not found"}, status=404)

# Filtering Views
class FilterByIngredient(APIView):
    def get(self, request):
        ingredient_name = request.query_params.get('ingredient')
        ingredients = Ingredient.objects.filter(name__icontains=ingredient_name)
        cocktails = Cocktail.objects.filter(ingredients__in=ingredients).distinct()
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

class FilterByAlcoholic(APIView):
    def get(self, request):
        alcoholic = request.query_params.get('alcoholic')
        cocktails = Cocktail.objects.filter(alcoholic=(alcoholic.lower() == 'true'))
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

class FilterByCategory(APIView):
    def get(self, request):
        category = request.query_params.get('category')
        cocktails = Cocktail.objects.filter(category__icontains=category)
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

class FilterByGlass(APIView):
    def get(self, request):
        glass_type = request.query_params.get('glass')
        cocktails = Cocktail.objects.filter(glass_type__icontains=glass_type)
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

# List Metadata Views
class ListCategories(APIView):
    def get(self, request):
        categories = Cocktail.objects.values_list('category', flat=True).distinct()
        return Response(categories)

class ListGlasses(APIView):
    def get(self, request):
        glasses = Cocktail.objects.values_list('glass_type', flat=True).distinct()
        return Response(glasses)

class ListIngredients(APIView):
    def get(self, request):
        ingredients = Ingredient.objects.values_list('name', flat=True).distinct()
        return Response(ingredients)

class ListAlcoholicFilters(APIView):
    def get(self, request):
        return Response(["True", "False"])
