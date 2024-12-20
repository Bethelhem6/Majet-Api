from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Review
from .serializer import ReviewSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        recipe_id = self.kwargs['recipe_id']
        return Review.objects.filter(recipe_id=recipe_id)

    def perform_create(self, serializer):
        recipe_id = self.kwargs['recipe_id']
        serializer.save(recipe_id=recipe_id, user=self.request.user)

class ReviewUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.all()

    def perform_update(self, serializer):
        if self.get_object().user != self.request.user:
            raise PermissionDenied("You do not have permission to update this review.")
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this review.")
        self.perform_destroy(instance)
        return Response({"message": "Review deleted successfully"}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()