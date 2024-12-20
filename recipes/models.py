from django.db import models

from api.models import CustomUser
from category.models import Category

# Create your models here.



class Recipe(models.Model):
    title =  models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='recipes')

    def __str__(self):
        return self.title