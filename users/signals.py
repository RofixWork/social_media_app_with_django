from .models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
@receiver(pre_save, sender=User)
def set_default_username(sender, instance, **kwargs):
    if not instance.username:
            email_username, _ = instance.email.split("@")
            instance.username = email_username.lower()