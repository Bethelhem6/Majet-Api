from rest_framework import serializers
from .models import Recipe, Category

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'user', 'category']
