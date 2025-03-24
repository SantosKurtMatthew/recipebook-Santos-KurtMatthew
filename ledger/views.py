from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Ingredient, Recipe, RecipeImage
from .forms import RecipeImageForm


# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    redirect_field_name = 'recipe_list.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = '__all__'
    template_name = 'recipe_form.html'


class ImageCreateView(CreateView):
    model = RecipeImage
    template_name = 'recipeimage_form.html'
    form_class = RecipeImageForm

    def get_initial(self):
        initial = super().get_initial()
        initial['recipe'] = Recipe.objects.get(pk=self.kwargs.get('pk'))
        return initial

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['pk'] = pk
        return context
