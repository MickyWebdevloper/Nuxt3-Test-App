from django.shortcuts import get_object_or_404
from rest_framework import generics

# from . import models
from .models import Course
from .serializers import CourseSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # serializer_class = CategoryItemSerializer


# class CategoryItemLIistAPIView(generics.ListAPIView):
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
