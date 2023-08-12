from django.db import models
from django.utils.timesince import timesince
from django.utils.translation import gettext_lazy as _

# from blog.models import Category


class Post(models.Model):
    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("Required"),
        max_length=255,
    )
    description = models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    is_active = models.BooleanField(
        verbose_name=_("Course visibility"),
        help_text=_("Course Post visibility"),
        default=True,
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    # def FORMAT(self):
    #     return timesince(self.created_at)

    def __str__(self):
        return self.title


# class Category(models.Model):
#     name = models.CharField(
#         verbose_name=_("Category Name"),
#         help_text=_("Required and unique"),
#         max_length=255,
#         unique=True,
#     )
#     slug = models.SlugField(verbose_name=_("Category safe URL"), max_length=255, unique=True)
#     is_active = models.BooleanField(default=True)

#     class Meta:
#         verbose_name = _("Category")
#         verbose_name_plural = _("Categories")

#     def __str__(self):
#         return self.name


# class Course(models.Model):
#     image = models.ImageField(
#         verbose_name=_("image"),
#         help_text=_("Upload a Course image"),
#         upload_to="course/",
#         default="images/default.png",
#     )
#     alt_text = models.CharField(
#         verbose_name=_("Alturnative text"),
#         help_text=_("Please add alturnative text"),
#         max_length=255,
#         null=True,
#         blank=True,
#     )
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="course_category")
#     title = models.CharField(
#         verbose_name=_("title"),
#         help_text=_("Required"),
#         max_length=255,
#     )
#     description = models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
#     slug = models.SlugField(max_length=255, unique=True)

#     is_active = models.BooleanField(
#         verbose_name=_("Course visibility"),
#         help_text=_("Course Post visibility"),
#         default=True,
#     )
#     created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
#     updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

#     class Meta:
#         ordering = ("-created_at",)
#         verbose_name = _("Course")
#         verbose_name_plural = _("Courses")

#     # def FORMAT(self):
#     #     return timesince(self.created_at)

#     def __str__(self):
#         return self.title
