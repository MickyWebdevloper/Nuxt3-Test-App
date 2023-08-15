from django.shortcuts import get_object_or_404
from rest_framework import generics

# from . import models
from .models import Post
from .serializers import PostSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class BlogPostListView(generics.ListAPIView):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer


# class CategoryListView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     # serializer_class = CategoryItemSerializer


# class CategoryLiteItemView(generics.ListAPIView):
#     serializer_class = CategoryItemSerializer

#     def get_queryset(self):
#         try:
#             category_name = get_object_or_404(Category, name=self.kwargs.get("category"))
#             return models.BlogPost.objects.filter(category=category_name)
#         except Category.DoesNotExist:
#             return models.BlogPost.objects.none()


# class CategoryItemView(generics.RetrieveAPIView):
#     lookup_field = "pk"
#     # lookup_field = "slug"
#     queryset = models.BlogPost.objects.all()
#     serializer_class = CategoryItemSerializer
