from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("sign-in", views.user_login_view, name="login"),
    path("sign-out", views.user_logout_view, name="logout"),
]
