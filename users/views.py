from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import UserLoginForm
from .models import User


# Create your views here.
class LoginView(FormView):
    template_name = "users/sign-in.html"
    form_class = UserLoginForm
    success_url = "/"

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


class UserLogoutView(LogoutView): ...


user_login_view = LoginView.as_view()
user_logout_view = UserLogoutView.as_view()
