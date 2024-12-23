from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe


class PERSON_GENDER(models.TextChoices):
    MALE = "male", "Male"
    FEMALE = "female", "Female"


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(max_length=100, blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        """
        Import signals to ensure they are loaded when the app is ready.
        """
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="users", default="users/default_avatar.jpg")
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(
        max_length=10, choices=PERSON_GENDER.choices, default=PERSON_GENDER.MALE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"
        ordering = ["-created_at"]

    def thumbnail(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.image.url}" width="50" style="border-radius:5px;" />'
            )
        return ""

    def __str__(self):
        return getattr(self.user, "username", "")
