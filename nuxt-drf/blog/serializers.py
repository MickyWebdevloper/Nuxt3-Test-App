from rest_framework.serializers import (
    HyperlinkedIdentityField,
    HyperlinkedRelatedField,
    ModelSerializer,
    SerializerMethodField,
)

from .models import BlogPost, BlogPostImage, Category


class BlogPostImageSerializer(ModelSerializer):
    class Meta:
        model = BlogPostImage
        fields = ["image", "alt_text"]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]
        # depth = 2


class BlogPostSerializer(ModelSerializer):
    blog_post_image = BlogPostImageSerializer(many=True, read_only=True)

    blog_post_category = HyperlinkedRelatedField(
        view_name="store:category_item", lookup_field="slug", many=True, read_only=True
    )

    detail_url = HyperlinkedIdentityField(view_name="store:product", lookup_field="slug")
    category_list = HyperlinkedIdentityField(view_name="store:category_list_item", lookup_field="category")

    category_name = SerializerMethodField(method_name="category")

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "detail_url",
            "category_list",
            "blog_post_category",
            "category_name",
            "title",
            "description",
            "slug",
            "blog_post_image",
        ]

    def category(self, obj):
        return obj.category.name


class CategoryItemSerializer(ModelSerializer):
    blog_post_image = BlogPostImageSerializer(many=True, read_only=True)

    detail_url = HyperlinkedIdentityField(view_name="store:category_item", lookup_field="pk")
    # category_list = HyperlinkedIdentityField(view_name="store:category_item", lookup_field="category")

    category_name = SerializerMethodField(method_name="category")

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "detail_url",
            # "category_list",
            # "blog_post_category",
            "category_name",
            "title",
            "description",
            "slug",
            "blog_post_image",
        ]

    def category(self, obj):
        return obj.category.name
