from django.db import models
from recipes.models import Recipe
from api.models import CustomUser
# Create your models here.

class Review(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.recipe.title}"