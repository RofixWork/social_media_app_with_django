from django.contrib import admin

from .models import Profile, User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff", "is_superuser")
    search_fields = ("username", "email")
    filter_fields = ("is_staff", "is_superuser")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "full_name", "thumbnail", "created_at", "updated_at")
    search_fields = ("user__username",)
    filter_fields = ("created_at", "updated_at")
