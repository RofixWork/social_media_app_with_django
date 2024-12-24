from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from posts.models import Post


# Create your views here.
class HomePageView(LoginRequiredMixin, ListView):
    template_name = "base/index.html"
    model = Post
    context_object_name = "posts"


home_page_view = HomePageView.as_view()
