from rest_framework import generics
from cocktail.models import Cocktail
from cocktail.serializers import CocktailSerializer
# import openpyxl


class CocktailList(generics.ListCreateAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer


class CocktailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

# from cocktail.models import Cocktail

# # Open the Excel file and select the active worksheet
# workbook = openpyxl.load_workbook('cocktails.xlsx')
# worksheet = workbook.active

# # Iterate over each row in the worksheet and create a list of Cocktail objects
# cocktails = []
# for row in worksheet.iter_rows(min_row=2, values_only=True):
#     name = row[0]
#     instructions = row[1]
#     image_data = row[2]
#     cocktail = Cocktail(name=name, instructions=instructions, image_data=image_data)
#     cocktails.append(cocktail)

# # Use bulk_create() to create all the Cocktail objects in the database at once
# Cocktail.objects.bulk_create(cocktails)
