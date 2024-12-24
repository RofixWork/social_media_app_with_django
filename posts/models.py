from autoslug import AutoSlugField
from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe


class LikedStatus(models.TextChoices):
    LIKED = "liked", "Liked"
    UNLIKED = "unliked", "Unliked"


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_posts"
    )
    title = models.CharField(max_length=100)
    slig = AutoSlugField(populate_from="title", unique=True, blank=True)
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

    def is_liked_by_user(self, user):
        return Liked.objects.filter(post=self, user=user).exists()

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title


class Liked(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_likes"
    )
    status = models.CharField(
        max_length=10, choices=LikedStatus.choices, default=LikedStatus.LIKED
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "liked"
        verbose_name_plural = "likes"
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(fields=["post", "user"], name="unique_like")
        ]

    def __str__(self):
        return f"{self.user} liked {self.post}"
