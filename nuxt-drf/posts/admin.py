from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "description",
        "slug",
        "is_active",
        "created_at",
        "updated_at",
    ]
    prepopulated_fields = {"slug": ["title"]}
