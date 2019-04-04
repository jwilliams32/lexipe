import requests
from bs4 import BeautifulSoup
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=500)
    ingredients = models.TextField(max_length=2000)
    directions = models.TextField(max_length=2000)
    author = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __int__(self):
        return '{0'.format(self.title)

    def get_absolute_url(self):
        return reverse('view_recipe', args=[str(self.id)])


class ScrapeRecipe(models.Model):
    url = models.CharField(max_length=1000)
