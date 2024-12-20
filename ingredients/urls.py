from django.urls import path
from .views import (
    get_all_ingredients, 
    create_ingredient, 
    get_ingredient_by_id, 
    update_ingredient, 
    delete_ingredient
)

urlpatterns = [
    path('ingredients/', get_all_ingredients, name='get-all-ingredients'),
    path('ingredients/create/', create_ingredient, name='create-ingredient'),
    path('ingredients/<int:ingredient_id>/', get_ingredient_by_id, name='get-ingredient-by-id'),
    path('ingredients/update/<int:ingredient_id>/', update_ingredient, name='update-ingredient'),
    path('ingredients/delete/<int:ingredient_id>/', delete_ingredient, name='delete-ingredient'),
]
