import os
import openpyxl
import requests
import base64
from io import BytesIO
from django.core.management.base import BaseCommand
from cocktail.models import Cocktail


class Command(BaseCommand):
    help = 'Import cocktails data from an Excel sheet'

    def handle(self, *args, **options):
        # Replace 'cocktails.xlsx' with the path to your Excel sheet
        wb = openpyxl.load_workbook('data/cocktails.xlsx')
        ws = wb.active

        # Create a folder to store the cocktail images
        os.makedirs('cocktail_images', exist_ok=True)

        for row in ws.iter_rows(min_row=2):
            drink = row[0].value
            DrinkAlternate = row[1].value
            Tags = row[2].value
            category = row[3].value
            IBA = row[4].value
            alcoholic = row[5].value
            glass = row[6].value
            instructions = row[7].value
            image_url = row[8].value
            Ingredient1 = row[9].value
            Ingredient2 = row[10].value
            Ingredient3 = row[11].value
            Ingredient4 = row[12].value
            Ingredient5 = row[13].value
            Ingredient6 = row[14].value
            Ingredient7 = row[15].value
            Ingredient8 = row[16].value
            Ingredient9 = row[17].value
            Ingredient10 = row[18].value
            Measure1 = row[19].value
            Measure2 = row[20].value
            Measure3 = row[21].value
            Measure4 = row[22].value
            Measure5 = row[23].value
            Measure6 = row[24].value
            Measure7 = row[25].value
            Measure8 = row[26].value

            # Download the cocktail image and save it to the 'cocktail_images' folder
            response = requests.get(image_url)
            image_data = response.content
            image_path = f'cocktail_images/{drink}.jpg'
            with open(image_path, 'wb') as f:
                f.write(image_data)

            # Encode the image data as base64
            encoded_image = base64.b64encode(image_data).decode('utf-8')

            # Create the cocktail object
            cocktail = Cocktail.objects.create(
                drink=drink,
                DrinkAlternate=DrinkAlternate,
                Tags=Tags,
                IBA=IBA,
                instructions=instructions,
                category=category,
                glass=glass,
                alcoholic=alcoholic,
                image=image_path,
                Ingredient1=Ingredient1,
                Ingredient2=Ingredient2,
                Ingredient3=Ingredient3,
                Ingredient4=Ingredient4,
                Ingredient5=Ingredient5,
                Ingredient6=Ingredient6,
                Ingredient7=Ingredient7,
                Ingredient8=Ingredient8,
                Ingredient9=Ingredient9,
                Ingredient10=Ingredient10,
                Measure1=Measure1,
                Measure2=Measure2,
                Measure3=Measure3,
                Measure4=Measure4,
                Measure5=Measure5,
                Measure6=Measure6,
                Measure7=Measure7,
                Measure8=Measure8,
            )

            # Save the cocktail image to the cocktail object
            cocktail.image.save(f'{drink}.jpg', BytesIO(
                base64.b64decode(encoded_image)))

        self.stdout.write(self.style.SUCCESS(
            'Successfully imported cocktails data'))
