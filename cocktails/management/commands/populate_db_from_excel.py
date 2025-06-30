import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from cocktails.models import Cocktail, Ingredient

class Command(BaseCommand):
    help = 'Populates the database from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='The path to the Excel file')

    def handle(self, *args, **options):
        excel_file_path = options['excel_file']

        try:
            df = pd.read_excel(excel_file_path)
        except FileNotFoundError:
            raise CommandError(f'Excel file not found at path: {excel_file_path}')
        except Exception as e:
            raise CommandError(f'Error reading Excel file: {e}')

        for index, row in df.iterrows():
            try:
                # Check if drink name is present and not empty
                drink_name = row.get('drink')
                if not drink_name or pd.isna(drink_name):
                    self.stdout.write(self.style.WARNING(f'Skipping row {index + 2} due to missing or empty drink name.'))
                    continue

                # Create or get ingredients
                ingredients = []
                for i in range(1, 11):  # Assuming max 10 ingredients based on Excel
                    ingredient_name = row.get(f'Ingredient{i}')
                    measure = row.get(f'Measure{i}')

                    if pd.notna(ingredient_name) and ingredient_name.strip():
                        # Combine measure and ingredient name for description if measure exists
                        description = f"{measure.strip()} {ingredient_name.strip()}" if pd.notna(measure) and measure.strip() else ingredient_name.strip()

                        ingredient, created = Ingredient.objects.get_or_create(
                            name=ingredient_name.strip(),
                            defaults={'description': description}
                        )
                        # Update description if ingredient already exists and description is different
                        if not created and ingredient.description != description:
                            ingredient.description = description
                            ingredient.save()
                        ingredients.append(ingredient)

                # Create or update cocktail
                cocktail, created = Cocktail.objects.update_or_create(
                    name=drink_name.strip(),
                    defaults={
                        'category': row.get('category'),
                        'glass_type': row.get('glass'),
                        'alcoholic': row.get('alcoholic') == 'Alcoholic',
                        'instructions': row.get('instructions'),
                        'image': row.get('image'),
                    }
                )
                cocktail.ingredients.set(ingredients)
                self.stdout.write(self.style.SUCCESS(f'Successfully processed cocktail: {cocktail.name}'))

            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Error processing row {index + 2}: {e}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated database from Excel file'))
