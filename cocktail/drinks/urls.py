from django.urls import path
from .views import (
    DrinkListView,
    DrinkSearchByNameView,
    search_by_ingredient,
    DrinkDetailView,
    DrinkFilterView,
    RandomDrinkView,
    LatestDrinksView,
)

urlpatterns = [
    path('drinks/', DrinkListView.as_view(), name='drink-list'),
    path('drinks/search/', DrinkSearchByNameView.as_view(), name='drink-search-by-name'),
    path('drinks/search-by-ingredient/', search_by_ingredient, name='drink-search-by-ingredient'),
    path('drinks/<pk>/', DrinkDetailView.as_view(), name='drink-detail'),
    path('drinks/filter/', DrinkFilterView.as_view(), name='drink-filter'),
    path('drinks/random-drink/', RandomDrinkView.as_view(), name='random-drink'),
    path('drinks/latest/', LatestDrinksView.as_view(), name='latest-drinks'),
]