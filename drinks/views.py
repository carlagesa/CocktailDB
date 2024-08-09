import requests
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Drink
from .serializers import DrinkSerializer

API_BASE_URL = "https://www.thecocktaildb.com/api/json/v1/1/"

def fetch_from_api(endpoint):
    url = f"{API_BASE_URL}{endpoint}"
    response = requests.get(url)
    return response.json()

class CocktailOnlyListView(APIView):
    def get(self, request):
        cocktails = Drink.objects.all()
        serializer = DrinkSerializer(cocktails, many=True)
        return Response(serializer.data)
    
class SearchCocktailByName(APIView):
    def get(self, request):
        name = request.GET.get('s')
        if not name:
            return Response({'detail': 'Name parameter is required'}, status=400)
        data = fetch_from_api(f"search.php?s={name}")
        return Response(data)

class ListCocktailsByFirstLetter(APIView):
    def get(self, request):
        letter = request.GET.get('f')
        if not letter:
            return Response({'detail': 'First letter parameter is required'}, status=400)
        data = fetch_from_api(f"search.php?f={letter}")
        return Response(data)

class SearchIngredientByName(APIView):
    def get(self, request):
        ingredient = request.GET.get('i')
        if not ingredient:
            return Response({'detail': 'Ingredient name parameter is required'}, status=400)
        data = fetch_from_api(f"search.php?i={ingredient}")
        return Response(data)

class LookupCocktailById(APIView):
    def get(self, request):
        cocktail_id = request.GET.get('i')
        if not cocktail_id:
            return Response({'detail': 'Cocktail ID parameter is required'}, status=400)
        data = fetch_from_api(f"lookup.php?i={cocktail_id}")
        return Response(data)

class LookupIngredientById(APIView):
    def get(self, request):
        ingredient_id = request.GET.get('iid')
        if not ingredient_id:
            return Response({'detail': 'Ingredient ID parameter is required'}, status=400)
        data = fetch_from_api(f"lookup.php?iid={ingredient_id}")
        return Response(data)

class LookupRandomCocktail(APIView):
    def get(self, request):
        data = fetch_from_api("random.php")
        return Response(data)

class FilterByIngredient(APIView):
    def get(self, request):
        ingredient = request.GET.get('i')
        if not ingredient:
            return Response({'detail': 'Ingredient parameter is required'}, status=400)
        data = fetch_from_api(f"filter.php?i={ingredient}")
        return Response(data)

class FilterByAlcoholic(APIView):
    def get(self, request):
        alcoholic = request.GET.get('a')
        if not alcoholic:
            return Response({'detail': 'Alcoholic parameter is required'}, status=400)
        data = fetch_from_api(f"filter.php?a={alcoholic}")
        return Response(data)

class FilterByCategory(APIView):
    def get(self, request):
        category = request.GET.get('c')
        if not category:
            return Response({'detail': 'Category parameter is required'}, status=400)
        data = fetch_from_api(f"filter.php?c={category}")
        return Response(data)

class FilterByGlass(APIView):
    def get(self, request):
        glass = request.GET.get('g')
        if not glass:
            return Response({'detail': 'Glass parameter is required'}, status=400)
        data = fetch_from_api(f"filter.php?g={glass}")
        return Response(data)

class ListCategories(APIView):
    def get(self, request):
        data = fetch_from_api("list.php?c=list")
        return Response(data)

class ListGlasses(APIView):
    def get(self, request):
        data = fetch_from_api("list.php?g=list")
        return Response(data)

class ListIngredients(APIView):
    def get(self, request):
        data = fetch_from_api("list.php?i=list")
        return Response(data)

class ListAlcoholicFilters(APIView):
    def get(self, request):
        data = fetch_from_api("list.php?a=list")
        return Response(data)
