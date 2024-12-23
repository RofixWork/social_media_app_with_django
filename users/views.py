from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import reverse_lazy
from django.views.generic import FormView

from utils.mixins import UserAlreadyLoggedIn

from .forms import UserLoginForm


# Create your views here.
class LoginView(UserAlreadyLoggedIn, FormView):
    template_name = "users/sign-in.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("base:home")

    def form_valid(self, form: UserLoginForm):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(
                None, "Invalid credentials"
            )  # Add a custom error message to the form.
            return self.form_invalid(form)


class UserChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/change-password.html"
    success_url = reverse_lazy("password_change_done")


class UserPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = "users/password-change-done.html"


class UserLogoutView(LogoutView): ...


class PasswordResetView(UserAlreadyLoggedIn, PasswordResetView):
    template_name = "users/password-reset.html"


class PasswordResetConfirmView(UserAlreadyLoggedIn, PasswordResetConfirmView):
    template_name = "users/password-reset-confirm.html"


class PasswordResetDoneView(UserAlreadyLoggedIn, PasswordResetDoneView):
    template_name = "users/password-reset-done.html"


class PasswordResetCompleteView(UserAlreadyLoggedIn, PasswordResetCompleteView):
    template_name = "users/password-reset-complete.html"


user_login_view = LoginView.as_view()
user_change_password_view = UserChangePasswordView.as_view()
user_password_change_done_view = UserPasswordChangeDoneView.as_view()
user_logout_view = UserLogoutView.as_view()
password_reset_view = PasswordResetView.as_view()
password_reset_confirm_view = PasswordResetConfirmView.as_view()
password_reset_done_view = PasswordResetDoneView.as_view()
password_reset_complete_view = PasswordResetCompleteView.as_view()
