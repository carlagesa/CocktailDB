from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status # Import status
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
        if not name:
            return Response({"error": "Query parameter 'name' is required."}, status=status.HTTP_400_BAD_REQUEST)
        cocktails = Cocktail.objects.filter(name__icontains=name)
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

class ListCocktailsByFirstLetter(APIView):
    def get(self, request):
        letter = request.query_params.get('letter')
        if not letter:
            return Response({"error": "Query parameter 'letter' is required."}, status=status.HTTP_400_BAD_REQUEST)
        cocktails = Cocktail.objects.filter(name__istartswith=letter)
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

class LookupCocktailById(APIView):
    def get(self, request):
        cocktail_id = request.query_params.get('id')
        if not cocktail_id:
            return Response({"error": "Query parameter 'id' is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            cocktail = Cocktail.objects.get(id=cocktail_id)
            serializer = CocktailSerializer(cocktail)
            return Response(serializer.data)
        except Cocktail.DoesNotExist:
            return Response({"error": "Cocktail not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"error": "Invalid 'id' format."}, status=status.HTTP_400_BAD_REQUEST)


class LookupRandomCocktail(APIView):
    def get(self, request):
        cocktail = Cocktail.objects.order_by('?').first()
        if cocktail:
            serializer = CocktailSerializer(cocktail)
            return Response(serializer.data)
        else:
            return Response({"error": "No cocktails available"}, status=status.HTTP_404_NOT_FOUND)

# Ingredient Views
class SearchIngredientByName(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        if not name:
            return Response({"error": "Query parameter 'name' is required."}, status=status.HTTP_400_BAD_REQUEST)
        ingredients = Ingredient.objects.filter(name__icontains=name)
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

class LookupIngredientById(APIView):
    def get(self, request):
        ingredient_id = request.query_params.get('id')
        if not ingredient_id:
            return Response({"error": "Query parameter 'id' is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            ingredient = Ingredient.objects.get(id=ingredient_id)
            serializer = IngredientSerializer(ingredient)
            return Response(serializer.data)
        except Ingredient.DoesNotExist:
            return Response({"error": "Ingredient not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"error": "Invalid 'id' format."}, status=status.HTTP_400_BAD_REQUEST)


# Filtering Views
class FilterByIngredient(APIView):
    def get(self, request):
        ingredient_name = request.query_params.get('ingredient')
        if not ingredient_name:
            return Response({"error": "Query parameter 'ingredient' is required."}, status=status.HTTP_400_BAD_REQUEST)
        ingredients = Ingredient.objects.filter(name__icontains=ingredient_name)
        cocktails = Cocktail.objects.filter(ingredients__in=ingredients).distinct()
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

class FilterByAlcoholic(APIView):
    def get(self, request):
        alcoholic_param = request.query_params.get('alcoholic')
        if alcoholic_param is None:
            return Response({"error": "Query parameter 'alcoholic' is required."}, status=status.HTTP_400_BAD_REQUEST)

        is_alcoholic_query = alcoholic_param.lower()
        if is_alcoholic_query in ['true', '1', 'yes']:
            filter_value = True
        elif is_alcoholic_query in ['false', '0', 'no']:
            filter_value = False
        else:
            return Response({"error": f"Invalid value for 'alcoholic' parameter: '{alcoholic_param}'. Use 'true' or 'false'."}, status=status.HTTP_400_BAD_REQUEST)

        cocktails = Cocktail.objects.filter(alcoholic=filter_value)
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

class FilterByCategory(APIView):
    def get(self, request):
        category = request.query_params.get('category')
        if not category:
            return Response({"error": "Query parameter 'category' is required."}, status=status.HTTP_400_BAD_REQUEST)
        cocktails = Cocktail.objects.filter(category__icontains=category)
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

class FilterByGlass(APIView):
    def get(self, request):
        glass_type = request.query_params.get('glass')
        if not glass_type:
            return Response({"error": "Query parameter 'glass' is required."}, status=status.HTTP_400_BAD_REQUEST)
        cocktails = Cocktail.objects.filter(glass_type__icontains=glass_type)
        serializer = CocktailSerializer(cocktails, many=True)
        return Response(serializer.data)

# List Metadata Views
class ListCategories(APIView):
    def get(self, request):
        categories = Cocktail.objects.values_list('category', flat=True).distinct()
        return Response(list(categories)) # Ensure it's a list for JSON

class ListGlasses(APIView):
    def get(self, request):
        glasses = Cocktail.objects.values_list('glass_type', flat=True).distinct()
        return Response(list(glasses)) # Ensure it's a list for JSON

class ListIngredients(APIView):
    def get(self, request):
        ingredients = Ingredient.objects.values_list('name', flat=True).distinct()
        return Response(list(ingredients)) # Ensure it's a list for JSON

class ListAlcoholicFilters(APIView):
    def get(self, request):
        return Response(["True", "False"])
