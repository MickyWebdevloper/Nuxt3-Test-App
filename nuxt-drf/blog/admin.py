from django.contrib import admin

from .models import BlogPost, BlogPostImage, Category

# from mptt.admin import MPTTModelAdmin


# admin.site.register(Category, MPTTModelAdmin)


# class ProductSpecificationInline(admin.TabularInline):
#     model = ProductSpecification


# @admin.register(ProductType)
# class ProductTypeAdmin(admin.ModelAdmin):
#     inlines = [
#         ProductSpecificationInline,
#     ]


class BlogPostImageInline(admin.TabularInline):
    model = BlogPostImage


# class BlogPostImageInline(admin.TabularInline):
#     model = BlogPostImage


# class ProductSpecificationValueInline(admin.TabularInline):
#     model = ProductSpecificationValue


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # fields = ["title", "description", "slug"]
    list_display = ["id", "name", "slug"]


@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):
    # fields = ["title", "description", "slug"]
    list_display = [
        "id",
        "title",
        "description",
        "slug",
        "category",
        "is_active",
        "created_at",
        "updated_at",
    ]
    prepopulated_fields = {"slug": ["title"]}

    inlines = [
        BlogPostImageInline,
    ]
