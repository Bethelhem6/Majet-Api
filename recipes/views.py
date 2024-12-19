from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Recipe
from .serializer import RecipeSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated]) 
def recipe_list_create(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer (recipes, many= True)
        return Response(serializer.data)
    

    if request.method == 'POST':
        data =  request.data.copy()
        data['user'] = request.user.id
        serializer = RecipeSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def get_recipe_by_id(request, recipe_id):
    try:
        recipe =  Recipe.objects.get(id = recipe_id)

        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Recipe.DoesNotExist:
        return Response({"error":"Recipe not found."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@permission_classes([IsAuthenticated]) 
def update_recipe(request, recipe_id):
    try:
        # Fetch the recipe by ID
        recipe = Recipe.objects.get(id=recipe_id, user=request.user)  # Ensure the user owns the recipe

        # Deserialize and validate data
        serializer = RecipeSerializer(recipe, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Recipe.DoesNotExist:
        return Response(
            {"error": "Recipe not found or you do not have permission to edit it."},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_recipe(request, recipe_id):
    try:
        # Fetch the recipe by ID
        recipe = Recipe.objects.get(id=recipe_id, user=request.user)  # Ensure the user owns the recipe
        recipe.delete()
        return Response({"message": "Recipe deleted successfully."}, status=status.HTTP_200_OK)
    except Recipe.DoesNotExist:
        return Response(
            {"error": "Recipe not found or you do not have permission to delete it."},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )