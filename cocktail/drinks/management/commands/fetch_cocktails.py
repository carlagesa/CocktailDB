import requests
from django.core.management.base import BaseCommand
from drinks.models import Drink

class Command(BaseCommand):
    help = 'Fetch cocktails from TheCocktailDB API'

    def handle(self, *args, **kwargs):
        url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s='
        response = requests.get(url)
        data = response.json()

        for item in data['drinks']:
            drink, created = Drink.objects.get_or_create(
                name=item['strDrink'],
                defaults={
                    'category': item['strCategory'],
                    'alcoholic': item['strAlcoholic'],
                    'glass': item['strGlass'],
                    'instructions': item['strInstructions'],
                    'image_url': item['strDrinkThumb'],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added drink: {drink.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Drink already exists: {drink.name}'))
