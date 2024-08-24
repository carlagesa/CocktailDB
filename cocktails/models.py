from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Cocktail(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    glass_type = models.CharField(max_length=100)
    alcoholic = models.BooleanField(default=True)
    instructions = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, related_name='cocktails')
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
