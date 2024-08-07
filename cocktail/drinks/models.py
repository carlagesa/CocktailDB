from django.db import models

class Drink(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    alcoholic = models.CharField(max_length=255)
    glass = models.CharField(max_length=255)
    instructions = models.TextField()
    thumbnail = models.URLField()
    ingredients = models.JSONField(default=list)  # JSON field to store a list of ingredients

    def __str__(self):
        return self.name