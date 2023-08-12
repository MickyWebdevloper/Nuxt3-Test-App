from django.urls import path

from .views import PostDetailAPIView, PostListAPIView

app_name = "post"

urlpatterns = [
    path("posts/", PostListAPIView.as_view(), name="posts"),
    path("posts/<slug:slug>/", PostDetailAPIView.as_view(), name="post-detail"),
    # path("api/categories/", CategoryListView.as_view(), name="categories"),
    # path("api/category-list/<slug:category>/", CategoryLiteItemView.as_view(), name="category_list_item"),
    # path("api/category-detail/<int:pk>/", CategoryItemView.as_view(), name="category_item"),
    # path("api/category-detail/<slug:slug>/", CategoryItemView.as_view(), name="category_item"),
]
