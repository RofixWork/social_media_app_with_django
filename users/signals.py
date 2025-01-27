from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Profile, User


@receiver(pre_save, sender=User)
def set_default_username(sender, instance, **kwargs):
    if not instance.username:
        email_username, _ = instance.email.split("@")
        instance.username = email_username.lower()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
