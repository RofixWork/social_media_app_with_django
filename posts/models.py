from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe
from autoslug import AutoSlugField

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_posts"
    )
    title = models.CharField(max_length=100)
    slig = AutoSlugField(populate_from='title', unique=True, blank=True)
    image = models.ImageField(upload_to="posts")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def thumbnail(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.image.url}" width="50" style="border-radius:5px;" />'
            )
        return ""

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title
