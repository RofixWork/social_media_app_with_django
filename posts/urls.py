from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("create/", views.create_new_post_view, name="create"),
    path('update/<int:post_id>/', views.update_post_view, name='update'),
    path("<int:post_id>/delete/", views.delete_post_view, name="delete"),  # Add this URL.
    path("<int:post_id>/like/", views.like_post_view, name="like"),  # Add this URL.
]
