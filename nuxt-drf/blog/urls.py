from django.urls import path

from .views import (
    BlogPost,
    BlogPostListView,
    CategoryItemView,
    CategoryListView,
    CategoryLiteItemView,
)

app_name = "store"

urlpatterns = [
    path("api/", BlogPostListView.as_view(), name="store_home"),
    path("api/<slug:slug>/", BlogPost.as_view(), name="product"),
    path("api/categories/", CategoryListView.as_view(), name="categories"),
    path("api/category-list/<slug:category>/", CategoryLiteItemView.as_view(), name="category_list_item"),
    path("api/category-detail/<int:pk>/", CategoryItemView.as_view(), name="category_item"),
    # path("api/category-detail/<slug:slug>/", CategoryItemView.as_view(), name="category_item"),
]
