from django.urls import path
from .views import ToggleFavoriteView, GetUserFavoritesView

urlpatterns = [
    path('api/favorites/toggle/', ToggleFavoriteView.as_view(), name='toggle-favorite'),
    path('api/users/favorites/', GetUserFavoritesView.as_view(), name='user-favorites'),
]
