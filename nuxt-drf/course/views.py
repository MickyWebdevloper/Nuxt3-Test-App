from django.shortcuts import get_object_or_404
from rest_framework import generics

# from . import models
from .models import Post
from .serializers import PostSerializer


class PostsListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class CourseListView(generics.ListAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer


# class CourseDetailView(generics.RetrieveAPIView):
#     lookup_field = "slug"
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer


# class CourseListItemView(generics.ListAPIView):
#     serializer_class = CourseSerializer

#     def get_queryset(self):
#         try:
#             category_name = get_object_or_404(Category, name=self.kwargs.get("category"))
#             return models.Course.objects.filter(category=category_name)
#         except Category.DoesNotExist:
#             return models.Course.objects.none()


# # class CourseItemView(generics.RetrieveAPIView):
# #     lookup_field = "slug"
# #     queryset = models.Course.objects.all()
# #     serializer_class = CourseSerializer
