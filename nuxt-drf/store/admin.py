from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Category,
    Product,
    ProductImage,
    ProductSpecification,
    ProductSpecificationValue,
    ProductType,
)

admin.site.register(Category, MPTTModelAdmin)


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationInline,
    ]


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # fields = ["title", "description", "slug"]
    list_display = [
        "id",
        "title",
        "description",
        "slug",
        "product_type",
        "category",
        "regular_price",
        "discount_price",
        "is_active",
        "created_at",
        "updated_at",
    ]
    prepopulated_fields = {"slug": ["title"]}

    inlines = [
        ProductSpecificationValueInline,
        ProductImageInline,
    ]
