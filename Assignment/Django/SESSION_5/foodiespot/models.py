from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    cuisine = models.CharField(max_length=20)
    rating = models.FloatField()
