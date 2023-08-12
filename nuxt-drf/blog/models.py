from django.db import models

# from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(verbose_name=_("Category safe URL"), max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


# class ProductType(models.Model):
#     name = models.CharField(verbose_name=_("Product Name"), help_text=_("Required"), max_length=255, unique=True)
#     is_active = models.BooleanField(default=True)

#     class Meta:
#         verbose_name = _("Product Type")
#         verbose_name_plural = _("Product Types")

#     def __str__(self):
#         return self.name

# class ProductSpecification(models.Model):
#     product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
#     name = models.CharField(verbose_name=_("Name"), help_text=_("Required"), max_length=255)

#     class Meta:
#         verbose_name = _("Product Specification")
#         verbose_name_plural = _("Product Specifications")

#     def __str__(self):
#         return self.name


class BlogPost(models.Model):
    # product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_category")
    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("Required"),
        max_length=255,
    )
    description = models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    slug = models.SlugField(max_length=255)

    is_active = models.BooleanField(
        verbose_name=_("Post visibility"),
        help_text=_("Change Post visibility"),
        default=True,
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Blog Post")
        verbose_name_plural = _("Blog Posts")

    # def get_absolute_url(self):
    #     print(";;;;;;;;;;;;;;;;;;----------------------")
    #     print(self.kwargs)
    #     print(";;;;;;;;;;;;;;;;;;----------------------")
    #     return reverse("store:product", kwargs={"str": self.name})

    def __str__(self):
        return self.title


# class ProductSpecificationValue(models.Model):
# product = models.ForeignKey(Product, on_delete=models.CASCADE)
# specification = models.ForeignKey(ProductSpecification, on_delete=models.RESTRICT)
# value = models.CharField(
#     verbose_name=_("value"),
#     help_text=_("Product specification value (maximum of 255 words"),
#     max_length=255,
# )

# class Meta:
#     verbose_name = _("Product Specification Value")
#     verbose_name_plural = _("Product Specification Values")

# def __str__(self):
#     return self.value


class BlogPostImage(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="blog_post_image")
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a product image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Alturnative text"),
        help_text=_("Please add alturnative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Blog Post Image")
        verbose_name_plural = _("Blog Post Images")
