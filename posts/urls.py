from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("create/", views.create_new_post_view, name="create"),  # Add this URL.
]
