from rest_framework.serializers import (
    HyperlinkedIdentityField,
    HyperlinkedRelatedField,
    ModelSerializer,
    SerializerMethodField,
)

from .models import Post


class PostSerializer(ModelSerializer):
    detail_url = HyperlinkedIdentityField(view_name="post:post-detail", lookup_field="slug")

    class Meta:
        model = Post
        fields = [
            "id",
            "detail_url",
            "title",
            "description",
            "slug",
            "created_at",
            "updated_at"
            # "blog_post_image",
        ]

    def category(self, obj):
        return obj.category.name


# class CategoryItemSerializer(ModelSerializer):
#     blog_post_image = BlogPostImageSerializer(many=True, read_only=True)

#     detail_url = HyperlinkedIdentityField(view_name="store:category_item", lookup_field="pk")
#     # category_list = HyperlinkedIdentityField(view_name="store:category_item", lookup_field="category")

#     category_name = SerializerMethodField(method_name="category")

#     class Meta:
#         model = BlogPost
#         fields = [
#             "id",
#             "detail_url",
#             # "category_list",
#             # "blog_post_category",
#             "category_name",
#             "title",
#             "description",
#             "slug",
#             "blog_post_image",
#         ]

#     def category(self, obj):
#         return obj.category.name
