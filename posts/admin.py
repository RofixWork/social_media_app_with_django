from django.contrib import admin

from .models import Liked, Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "thumbnail", "user", "created_at")
    search_fields = ("title", "content")
    filter_fields = ("user", "created_at", "updated_at")
    list_display_links = ("title",)


@admin.register(Liked)
class LikedAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_at")
    search_fields = ("post__title", "user__username")
    filter_fields = ("post", "user", "created_at")
