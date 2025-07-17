import requests
from django.core.management.base import BaseCommand
from django.db import transaction
from cocktails.models import Cocktail, Ingredient
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Command(BaseCommand):
    help = 'Populates the database with cocktail data from TheCocktailDB API'

    def handle(self, *args, **options):
        self.stdout.write("Starting to populate the database from TheCocktailDB API...")

        # The API endpoint to fetch cocktails starting with a specific letter
        base_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?f="
        
        # Fetch cocktails for each letter of the alphabet
        for letter in "abcdefghijklmnopqrstuvwxyz":
            self.stdout.write(f"Fetching cocktails starting with '{letter}'...")
            try:
                response = requests.get(f"{base_url}{letter}")
                response.raise_for_status()  # Raise an exception for bad status codes
                data = response.json()
                cocktails = data.get('drinks')

                if not cocktails:
                    self.stdout.write(self.style.WARNING(f"No cocktails found starting with '{letter}'."))
                    continue

                with transaction.atomic():
                    for cocktail_data in cocktails:
                        # Skip if cocktail already exists
                        if Cocktail.objects.filter(name=cocktail_data['strDrink']).exists():
                            continue

                        # Create Cocktail instance
                        cocktail, created = Cocktail.objects.update_or_create(
                            name=cocktail_data['strDrink'],
                            defaults={
                                'category': cocktail_data.get('strCategory', ''),
                                'glass_type': cocktail_data.get('strGlass', ''),
                                'alcoholic': cocktail_data.get('strAlcoholic') == 'Alcoholic',
                                'instructions': cocktail_data.get('strInstructions', ''),
                                'image': cocktail_data.get('strDrinkThumb', ''),
                            }
                        )

                        # Add ingredients
                        for i in range(1, 16):
                            ingredient_name = cocktail_data.get(f'strIngredient{i}')
                            if ingredient_name:
                                ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_name)
                                cocktail.ingredients.add(ingredient)
                        
                        if created:
                            logging.info(f"Created cocktail: {cocktail.name}")

            except requests.exceptions.RequestException as e:
                self.stdout.write(self.style.ERROR(f"Error fetching data for letter '{letter}': {e}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"An error occurred while processing letter '{letter}': {e}"))

        self.stdout.write(self.style.SUCCESS('Database successfully populated with cocktail data.'))