import os
import sys
import django
import requests

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cocktaildb.settings')
django.setup()

from cocktails.models import Cocktail, Ingredient

# URL for fetching cocktail data
url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s='

def save_cocktail(cocktail_data):
    # Extract ingredients
    ingredient_names = [cocktail_data.get(f'strIngredient{i}') for i in range(1, 11) if cocktail_data.get(f'strIngredient{i}')]

    # Save or retrieve ingredients
    ingredients = []
    for name in ingredient_names:
        ingredient, created = Ingredient.objects.get_or_create(name=name)
        ingredients.append(ingredient)

    # Create cocktail
    cocktail = Cocktail(
        name=cocktail_data['strDrink'],
        category=cocktail_data['strCategory'],
        glass_type=cocktail_data['strGlass'],
        alcoholic=(cocktail_data['strAlcoholic'] == 'Alcoholic'),
        instructions=cocktail_data['strInstructions'],
        image=cocktail_data['strDrinkThumb']
    )
    cocktail.save()
    
    # Add ingredients to cocktail
    cocktail.ingredients.set(ingredients)

def scrape_data():
    # Loop through letters a-z
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        params = {'s': letter}
        response = requests.get(url, params=params)
        data = response.json()

        if 'drinks' in data:
            for cocktail_data in data['drinks']:
                save_cocktail(cocktail_data)

if __name__ == "__main__":
    scrape_data()
