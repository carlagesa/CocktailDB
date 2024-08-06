# drinks/urls.py
from django.urls import path
from .views import DrinkListCreateView, DrinkDetailView

urlpatterns = [
    path('drinks/', DrinkListCreateView.as_view(), name='drink-list-create'),
    path('drinks/<pk>/', DrinkDetailView.as_view(), name='drink-detail'),
]
