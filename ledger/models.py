from django.db import models
from django.urls import reverse


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[self.pk])


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=255)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )


class RecipeImage(models.Model):
    recipe_image = models.ImageField(null=False, upload_to='images/')
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='images'
    )

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[self.recipe.pk])