from rest_framework.serializers import (
    HyperlinkedIdentityField,
    HyperlinkedRelatedField,
    ModelSerializer,
    SerializerMethodField,
)

from .models import Category, Product, ProductImage


class ImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image", "alt_text"]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]
        # depth = 2


class ProductSerializer(ModelSerializer):
    product_image = ImageSerializer(many=True, read_only=True)

    # children = CategorySerializer(many=True, read_only=True)

    product_category = HyperlinkedRelatedField(
        view_name="store:category_item", lookup_field="slug", many=True, read_only=True
    )

    detail_url = HyperlinkedIdentityField(view_name="store:product", lookup_field="slug")
    product_category = HyperlinkedIdentityField(view_name="store:category_item", lookup_field="slug")
    category_name = SerializerMethodField(method_name="category")

    class Meta:
        model = Product
        fields = [
            # "children",
            "id",
            "detail_url",
            "product_category",
            # "category",
            "category_name",
            "title",
            "description",
            "slug",
            "product_image",
        ]

    def category(self, obj):
        return obj.category.name
