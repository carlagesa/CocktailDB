from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Cocktail(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    category = models.CharField(max_length=100, db_index=True)
    glass_type = models.CharField(max_length=100) # db_index might be useful if filtered often
    alcoholic = models.BooleanField(default=True)
    instructions = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, related_name='cocktails')
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
