# ledger/urls.py

from django.urls import path
from .views import (
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    ImageCreateView,
    )

urlpatterns = [
    path('recipes/list/', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/add/', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<int:pk>/add_image', ImageCreateView.as_view(), name='image_create'),
]

# This might be needed, depending on your Django version
app_name = "ledger"
