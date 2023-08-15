from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("store.urls", namespace="store")),
    # path("", include("blog.urls", namespace="blog")),
    # path("", include("course.urls", namespace="post")),
    path("api/", include("posts.urls", namespace="posts")),
    # path("api/", include("tutorial.urls", namespace="tutorial")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
