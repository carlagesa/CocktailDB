import requests
from drinks.models import Drink

def fetch_cocktails():
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
            print(f'Successfully added drink: {drink.name}')
        else:
            print(f'Drink already exists: {drink.name}')
