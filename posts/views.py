from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, View

from .models import Liked, Post


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


class LikedPostView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, post_id: int):
        post = get_object_or_404(Post, id=post_id)
        like = Liked.objects.filter(post=post, user=request.user).first()

        if like:
            like.delete()
            # return json
            return JsonResponse(
                {"liked": False, "count": post.likes.count()}, status=200
            )
        else:
            Liked.objects.create(post=post, user=request.user)
            return JsonResponse(
                {"liked": True, "count": post.likes.count()}, status=200
            )


create_new_post_view = CreatePostView.as_view()
like_post_view = LikedPostView.as_view()
