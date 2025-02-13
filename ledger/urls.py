# ledger/urls.py

from django.urls import path
from .views import recipesList, recipe1, recipe2

urlpatterns = [
	path('recipes/list/', recipesList, name='recipesList'),
	path('recipe/1/', recipe1, name='recipe1'),
	path('recipe/2/', recipe2, name='recipe2'),
]

# This might be needed, depending on your Django version
app_name = "ledger"