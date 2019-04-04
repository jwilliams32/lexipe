from django.forms import ModelForm
from .models import ScrapeRecipe


class ParseForm(ModelForm):
    class Meta:
        model = ScrapeRecipe
        fields = ['url']

