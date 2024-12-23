from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Post


# Create your views here.
class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = "posts/create-post.html"
    model = Post
    fields = ("image", "title", "content")
    success_url = reverse_lazy("base:home")

    def form_valid(self, form):

        form.instance.user = self.request.user
        messages.success(
            self.request, "Post created successfully!"
        )  # Add success message.

        return super().form_valid(form)


create_new_post_view = CreatePostView.as_view()
