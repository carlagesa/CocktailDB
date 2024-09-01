from rest_framework import serializers
from .models import Cocktail, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'description']

class CocktailSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)  # Serialize ingredients as a list

    class Meta:
        model = Cocktail
        fields = ['id', 'name', 'category', 'glass_type', 'alcoholic', 'instructions', 'ingredients', 'image']
