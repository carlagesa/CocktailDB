from django.urls import path
from .views import (
    CocktailOnlyListView, SearchCocktailByName, ListCocktailsByFirstLetter,
    SearchIngredientByName, LookupCocktailById, LookupIngredientById,
    LookupRandomCocktail, FilterByIngredient, FilterByAlcoholic, FilterByCategory,
    FilterByGlass, ListCategories, ListGlasses, ListIngredients, ListAlcoholicFilters,
    IngredientCreateView, CocktailCreateView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('cocktails-only/', CocktailOnlyListView.as_view(), name='cocktails-only-list'),
    path('search/cocktail/', SearchCocktailByName.as_view(), name='search-cocktail-by-name'),
    path('search/letter/', ListCocktailsByFirstLetter.as_view(), name='list-cocktails-by-first-letter'),
    path('search/ingredient/', SearchIngredientByName.as_view(), name='search-ingredient-by-name'),
    path('lookup/cocktail/', LookupCocktailById.as_view(), name='lookup-cocktail-by-id'),
    path('lookup/ingredient/', LookupIngredientById.as_view(), name='lookup-ingredient-by-id'),
    path('random/cocktail/', LookupRandomCocktail.as_view(), name='lookup-random-cocktail'),
    path('filter/ingredient/', FilterByIngredient.as_view(), name='filter-by-ingredient'),
    path('filter/alcoholic/', FilterByAlcoholic.as_view(), name='filter-by-alcoholic'),
    path('filter/category/', FilterByCategory.as_view(), name='filter-by-category'),
    path('filter/glass/', FilterByGlass.as_view(), name='filter-by-glass'),
    path('list/categories/', ListCategories.as_view(), name='list-categories'),
    path('list/glasses/', ListGlasses.as_view(), name='list-glasses'),
    path('list/ingredients/', ListIngredients.as_view(), name='list-ingredients'),
    path('list/alcoholic/', ListAlcoholicFilters.as_view(), name='list-alcoholic-filters'),
    path('ingredients/', IngredientCreateView.as_view(), name='ingredient-create'),
    path('cocktails/', CocktailCreateView.as_view(), name='cocktail-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
