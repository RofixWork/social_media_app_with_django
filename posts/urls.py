from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("create/", views.create_new_post_view, name="create"),
    path("<int:post_id>/like/", views.like_post_view, name="like"),  # Add this URL.
]
