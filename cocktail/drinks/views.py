# drinks/views.py
from rest_framework import generics, permissions
from .models import Drink
from .serializers import DrinkSerializer

class DrinkListCreateView(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = [permissions.IsAuthenticated]

class DrinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = [permissions.IsAuthenticated]
