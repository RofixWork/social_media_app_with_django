from django.shortcuts import redirect
from django.urls import reverse_lazy


class UserAlreadyLoggedIn:
    redirect_url = reverse_lazy("base:home")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(
                self.redirect_url
            )  # Redirect to home page if user is already logged in.
        return super(UserAlreadyLoggedIn, self).dispatch(request, *args, **kwargs)
