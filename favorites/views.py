from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from recipes.serializer import RecipeSerializer
from .models import Favorite
from .serializer import FavoriteSerializer

class GetUserFavoritesView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        favorites = Favorite.objects.filter(user=user).select_related('recipe')
        
        # Serialize favorite recipes
        favorite_recipes = [favorite.recipe for favorite in favorites]
        
        # Here you could create a serializer to return more detailed information about each recipe
        serializer = RecipeSerializer(favorite_recipes, many=True)

        return Response(serializer.data, status=200)
    

class ToggleFavoriteView(generics.GenericAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        recipe_id = request.data.get('recipe')

        if not recipe_id:
            return Response({"detail": "Recipe ID is required."}, status=400)

        # Check if the recipe is already a favorite
        favorite = Favorite.objects.filter(user=user, recipe_id=recipe_id).first()

        if favorite:
            # If it exists, remove it
            favorite.delete()
            return Response({"message": "Recipe removed from favorites."}, status=200)
        else:
            # Otherwise, add it
            Favorite.objects.create(user=user, recipe_id=recipe_id)
            return Response({"message": "Recipe added to favorites."}, status=201)