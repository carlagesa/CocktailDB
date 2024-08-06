from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    alcoholic = models.CharField(max_length=10)
    glass = models.CharField(max_length=100)
    instructions = models.TextField()
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name
