from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from . import models
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Product(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryItemView(generics.ListAPIView):
    # lookup_field = "slug"
    serializer_class = ProductSerializer

    def get_queryset(self):
        try:
            category = Category.objects.get(name=self.kwargs["slug"])
            descendants = category.get_descendants(include_self=True)
            if descendants.exists():
                return models.Product.objects.filter(category__in=descendants)
            else:
                return models.Product.objects.none()
        except Category.DoesNotExist:
            return models.Product.objects.none()

    def list(self, request, *args, **kwargs):
        """
        Retrieve the list of products for the specified category and its descendants.

        Returns:
            Response: A response containing the serialized data of products.
                      If the category or any descendants do not exist, it returns a custom JSON response.
        """
        queryset = self.get_queryset()

        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)

        else:
            return Response({"message": "This category has no Products."}, status=status.HTTP_200_OK)

    # def get_queryset(self):
    #     return models.Product.objects.filter(
    #         category__in=Category.objects.get(slug=self.kwargs["slug"]).get_descendants(include_self=True)
    #     )


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(level=1)
    serializer_class = CategorySerializer
