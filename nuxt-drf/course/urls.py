from django.urls import path

from .views import PostsListView

# CourseDetailView, CourseListView, PostDeatilView,

# CourseItemView,

app_name = "post"

urlpatterns = [
    path("posts/", PostsListView.as_view(), name="posts"),
    # path("courses/", CourseListView.as_view(), name="courses"),
    # path("courses/<slug:slug>/", CourseDetailView.as_view(), name="course"),
    # path("courses/list/<slug:category>/", CourseListItemView.as_view(), name="course_list_item"),
]
# path("courses/detail/<slug:slug>/", CourseItemView.as_view(), name="course_item"),
