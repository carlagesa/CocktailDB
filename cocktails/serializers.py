from rest_framework import serializers
from .models import Cocktail, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'description']

class CocktailSerializer(serializers.ModelSerializer):
    # For read operations, we want to see the details of the ingredients.
    # The IngredientSerializer will be used for each ingredient in the list.
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Cocktail
        # Explicitly list all fields that should be part of the Cocktail representation.
        # This includes the 'ingredients' field which will be populated by the nested serializer.
        fields = ['id', 'name', 'category', 'glass_type', 'alcoholic', 'instructions', 'image', 'ingredients']
