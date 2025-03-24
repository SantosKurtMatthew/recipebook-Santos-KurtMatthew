from django import forms

from .models import RecipeImage


class RecipeImageForm(forms.Form):
	class Meta:
		model = RecipeImage
		fields = '__all__'
		widgets = {
		}