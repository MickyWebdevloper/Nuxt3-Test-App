from django.contrib import admin

from .models import Post

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     # fields = ["title", "description", "slug"]
#     list_display = ["id", "name", "slug"]


@admin.register(Post)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    list_display = (
        "title",
        "description",
        "slug",
        "created_at",
    )
