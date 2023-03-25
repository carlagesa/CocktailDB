from django.db import models

IS_ALCOHOLIC = (
    ("Alcoholic", "Alcoholic"),
    ("Non-Alcoholic", "Non-Alcoholic"),

)

class Cocktail(models.Model):
    drink = models.CharField(max_length=100)
    DrinkAlternate = models.CharField(max_length=100, null=True)
    Tags = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    IBA  = models.CharField(max_length=100, blank=True, null=True) 
    alcoholic = models.CharField(max_length=16,choices=IS_ALCOHOLIC, null=True) 
    glass = models.CharField(max_length=50, null=True)
    instructions = models.TextField()
    image = models.ImageField(upload_to='cocktail_images', blank=True, null=True)
    Ingredient1 = models.CharField(max_length=50)
    Ingredient2 = models.CharField(max_length=50)
    Ingredient3 = models.CharField(max_length=50, null=True)
    Ingredient4 = models.CharField(max_length=50, null=True)
    Ingredient5 = models.CharField(max_length=50, null=True)
    Ingredient6 = models.CharField(max_length=50, null=True)
    Ingredient7 = models.CharField(max_length=50, null=True)
    Ingredient8 = models.CharField(max_length=50, null=True)
    Ingredient9 = models.CharField(max_length=50, null=True)
    Ingredient10 = models.CharField(max_length=50, null=True)
    Measure1 = models.CharField(max_length=50, null=True)
    Measure2 = models.CharField(max_length=50, null=True)
    Measure3 = models.CharField(max_length=50, null=True)
    Measure4 = models.CharField(max_length=50, null=True)
    Measure5 = models.CharField(max_length=50, null=True)
    Measure6 = models.CharField(max_length=50, null=True)
    Measure7 = models.CharField(max_length=50, null=True)
    Measure8 = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.drink
