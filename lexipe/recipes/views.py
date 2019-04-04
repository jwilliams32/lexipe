from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, FormView
from .forms import ParseForm
from .models import Recipe
from django.http import HttpResponseRedirect
from .recipe_scraper import ParseRecipe
from django.shortcuts import render
# Create your views here.


class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['title', 'ingredients', 'directions', 'author']
    template_name = 'recipes/recipe_form.html'
    context_object_name = ''

    def form_valid(self, form):
        form.instance = form.save(commit=False)
        return super().form_valid(form)


def scrape_recipe(request):
    if request.method == 'POST':
        form = ParseForm(request.POST)
        if form.is_valid():
            form.instance = form.save(commit=False)
            url = form.cleaned_data['url']
            new_recipe = Recipe()
            format_recipe = ParseRecipe(url)
            new_recipe.title = format_recipe.site_parser().title
            new_recipe.ingredients = format_recipe.site_parser().ingredients
            new_recipe.directions = format_recipe.site_parser().directions
            if format_recipe.site_parser().author:
                new_recipe.author = format_recipe.site_parser().author
            else:
                new_recipe.author = ''
            new_recipe.save()
        return HttpResponseRedirect('/recipes')
    else:
        form = ParseForm()
        return render(request, 'recipes/scrape.html', {'form': form})


class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['title', 'ingredients', 'directions', 'author']
    template_name = 'recipes/recipe_form.html'
    context_object_name = ''

    def form_valid(self, form):
        form.instance = form.save(commit=False)
        return super().form_valid(form)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/view_recipe.html'
    context_object_name = 'recipe'


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = '/recipes'
#
# def list_recipes(request):
#     recipes = Recipe.objects.all
#     return render(request, 'recipes/list_recipes.html', {'recipes': recipes})


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/list_recipes.html'
    context_object_name = 'recipes'




# def edit_recipe(request, pk=None):
#     instance = get_object_or_404(Post)
#     form = forms.CreateRecipe(request.POST or None, instance=instance)
#     if form.is_valid():
#         instance = form.save(commit=False)
#     # instance = request.user
#         instance.save()
#         context = {
#             ""
#         }
#
#         recipe = Recipe.objects.filter(pk=pk).first()
#         form = forms.
#     else:
#         recipe = request.recipe
#     return render(request, 'recipes/edit_recipes.html', {'recipe': recipe})

# def list_recipes(request):
#     recipes = Recipe.object.all
#     return render(request, 'recipes/list_recipes', {'recipes': recipes})