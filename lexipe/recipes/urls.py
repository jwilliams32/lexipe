from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView, DeleteView, scrape_recipe
from . import views

urlpatterns = [
    path('recipes/', RecipeListView.as_view(), name='list_recipes'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='view_recipe'),
    path('recipe/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe_update'),
    # path('recipe/<int:pk>', views.view_recipe, name='view_recipe'),
    path('recipe/scrape', scrape_recipe, name='recipe_scrape'),
    path('recipes/create/', RecipeCreateView.as_view(), name='recipe_form'),
    path('recipe/<int:pk>/delete/', DeleteView.as_view(), name='recipe_delete')
    # path('recipes/test')
]