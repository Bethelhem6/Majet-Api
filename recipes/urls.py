from django.urls import path
from .views import recipe_list_create,get_recipe_by_id,update_recipe,delete_recipe

urlpatterns = [
    path('recipes/', recipe_list_create,name='recipe-list-create'),
    path('recipes/<int:recipe_id>/', get_recipe_by_id,name='get-recipe-by-id'),
    path('recipes/update/<int:recipe_id>/', update_recipe,name='update-recipe'),
    path('recipes/delete/<int:recipe_id>/', delete_recipe,name='delete-recipe'),

]