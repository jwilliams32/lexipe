from bs4 import BeautifulSoup
import sys
import requests
from . import models
sys.path.append('..')

# Create your models here.


class ParseRecipe:

    def __init__(self, url):
        self.url = url

    def site_parser(self):
        # session = requests.session()
        # session.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0"}
        # url = 'https://www.allrecipes.com/recipe/22848/ashleys-chocolate-chip-cookies/'
        # website = session.get(url)
        # soup = BeautifulSoup(website.text, 'html.parser')
        website = requests.get(self.url)
        soup = BeautifulSoup(website.text, 'lxml')
        recipe = dict()
        if "allrecipes" in website.url:
            recipe['recipe_title'] = soup.find("h1", {"id": "recipe-main-content"}).text
            recipe['author'] = soup.find("span", class_="submitter__name").text
            ingredients = []
            directions = []

            for ingredient in soup.find_all("span", class_="recipe-ingred_txt"):
                ingredients.append(ingredient.text)
            for span in soup.find_all("span", class_="recipe-directions__list--item"):
                directions.append(span.text)

            recipe['ingredients'] = ingredients
            recipe['directions'] = directions

            format_recipe = ReformatRecipe(recipe)

            new_recipe = models.Recipe()
            new_recipe.title = format_recipe.get_title()
            new_recipe.directions = format_recipe.get_directions()
            new_recipe.ingredients = format_recipe.get_ingredients()
            new_recipe.author = format_recipe.get_author()

        return new_recipe


class ReformatRecipe:

    def __init__(self, recipe):
        self.recipe = recipe

    def get_title(self):
        title = self.recipe['recipe_title']
        return title

    def get_ingredients(self):
        ingredients = self.recipe['ingredients']
        return ingredients

    def get_directions(self):
        directions = self.recipe['directions']
        return directions

    def get_author(self):
        author = self.recipe['author']
        return author

#     TODO
# class ParseMeasurements(self):
# place each measurement in a variable
# convert str to an int
# convert fraction to whole number
# calculate adding multiple recipes
# convert whole numbers and fractions back to string
# return the results
