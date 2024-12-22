from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(max_length=100, blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        """
        Import signals to ensure they are loaded when the app is ready.
        """
        return self.username
