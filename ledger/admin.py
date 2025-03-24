from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage


# Register your models here.
class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


class RecipeIngredientAdmin(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageAdmin(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientAdmin, RecipeImageAdmin]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
