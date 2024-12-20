from django.urls import path
from .views import ReviewListCreateView, ReviewUpdateDeleteView

urlpatterns = [
    path('recipes/<int:recipe_id>/reviews/', ReviewListCreateView.as_view(), name='recipe-reviews'),
    path('reviews/<int:pk>/', ReviewUpdateDeleteView.as_view(), name='review-detail'),
]
