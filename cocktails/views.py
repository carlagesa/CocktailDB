from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Cocktail, Ingredient
from .serializers import CocktailSerializer, IngredientSerializer
import random

class CocktailOnlyListView(generics.ListAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

class SearchCocktailByName(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        if not name:
            return Response({"error": "Name parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        cocktails = Cocktail.objects.filter(name__icontains=name)
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

class ListCocktailsByFirstLetter(APIView):
    def get(self, request):
        letter = request.query_params.get('letter')
        if not letter:
            return Response({"error": "Letter parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        cocktails = Cocktail.objects.filter(name__istartswith=letter)
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

class LookupCocktailById(APIView):
    def get(self, request):
        cocktail_id = request.query_params.get('id')
        if not cocktail_id:
            return Response({"error": "ID parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            cocktail = Cocktail.objects.get(id=cocktail_id)
            serializer = CocktailSerializer(cocktail)
            return Response(serializer.data)
        except Cocktail.DoesNotExist:
            return Response({"error": "Cocktail not found"}, status=status.HTTP_404_NOT_FOUND)

class LookupRandomCocktail(APIView):
    def get(self, request):
        cocktails = Cocktail.objects.all()
        if cocktails.exists():
            cocktail = random.choice(cocktails)
            serializer = CocktailSerializer(cocktail)
            return Response(serializer.data)
        else:
            return Response({"error": "No cocktails available"}, status=status.HTTP_404_NOT_FOUND)

class SearchIngredientByName(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        if not name:
            return Response({"error": "Name parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        ingredients = Ingredient.objects.filter(name__icontains=name)
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

class LookupIngredientById(APIView):
    def get(self, request):
        ingredient_id = request.query_params.get('id')
        if not ingredient_id:
            return Response({"error": "ID parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            ingredient = Ingredient.objects.get(id=ingredient_id)
            serializer = IngredientSerializer(ingredient)
            return Response(serializer.data)
        except Ingredient.DoesNotExist:
            return Response({"error": "Ingredient not found"}, status=status.HTTP_404_NOT_FOUND)

class FilterByIngredient(APIView):
    def get(self, request):
        ingredient_name = request.query_params.get('ingredient')
        if not ingredient_name:
            return Response({"error": "Ingredient parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        ingredients = Ingredient.objects.filter(name__icontains=ingredient_name)
        cocktails = Cocktail.objects.filter(ingredients__in=ingredients).distinct()
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

class FilterByAlcoholic(APIView):
    def get(self, request):
        alcoholic = request.query_params.get('alcoholic')
        if alcoholic not in ['true', 'false']:
            return Response({"error": "Invalid value for alcoholic filter"}, status=status.HTTP_400_BAD_REQUEST)
        cocktails = Cocktail.objects.filter(alcoholic=(alcoholic.lower() == 'true'))
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

class FilterByCategory(APIView):
    def get(self, request):
        category = request.query_params.get('category')
        if not category:
            return Response({"error": "Category parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        cocktails = Cocktail.objects.filter(category__icontains=category)
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

class FilterByGlass(APIView):
    def get(self, request):
        glass_type = request.query_params.get('glass')
        if not glass_type:
            return Response({"error": "Glass parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        cocktails = Cocktail.objects.filter(glass_type__icontains=glass_type)
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

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

class IngredientCreateView(generics.CreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class CocktailCreateView(generics.CreateAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer
