from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.get_categories, name='get-categories'),
    path('category/<int:category_id>/', views.get_category_by_id, name='get-category-by-id'),

]
