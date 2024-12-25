from django.db import models
from django.conf import settings
from recipes.models import Recipe

# Create your models here.

class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="favorites", on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, related_name="favorited_by", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f"{self.user} favorited {self.recipe}"