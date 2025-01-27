from django.urls import path

from . import views

urlpatterns = [
    path("sign-up", views.user_register_view, name="register"),
    path("sign-in", views.user_login_view, name="login"),
    path(
        "change-password", views.user_change_password_view, name="change_password"
    ),  # Add this URL.
    path(
        "password-change-done",
        views.user_password_change_done_view,
        name="password_change_done",
    ),  # Add this URL.
    path(
        "password-reset",
        views.password_reset_view,
        name="password_reset",
    ),  # Add this URL.
    path(
        "reset/<uidb64>/<token>",
        views.password_reset_confirm_view,
        name="password_reset_confirm",
    ),  # Add this URL.
    path(
        "password-reset/done",
        views.password_reset_done_view,
        name="password_reset_done",
    ),  # Add this URL.
    path(
        "password-reset/complete",
        views.password_reset_complete_view,
        name="password_reset_complete",
    ),  # Add this URL.
    path("sign-out", views.user_logout_view, name="logout"),  # Add this URL.
    path("profile/<int:pk>", views.user_profile_view, name="profile"),  # Add this URL.
    path("profile/<int:pk>/edit", views.edit_profile_view, name="edit_profile"),
]
