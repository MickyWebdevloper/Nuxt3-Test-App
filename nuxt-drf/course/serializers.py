from rest_framework.serializers import (  # HyperlinkedRelatedField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
)

from .models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "description", "slug", "created_at", "updated_at"]


# class CourseSerializer(ModelSerializer):
#     """
#     nothing to say
#     """

#     detail_url = HyperlinkedIdentityField(view_name="course:course", lookup_field="slug")
#     # category_list = HyperlinkedIdentityField(view_name="course:course_list_item",
#     #                                           lookup_field="category")

#     category_name = SerializerMethodField(method_name="category")

#     class Meta:
#         model = Course
#         fields = [
#             "id",
#             "detail_url",
#             # "category_list",
#             "category_name",
#             "image",
#             "alt_text",
#             "title",
#             "description",
#             "slug",
#             "created_at",
#             "updated_at",
#         ]

#     def category(self, obj):
#         return obj.category.name
