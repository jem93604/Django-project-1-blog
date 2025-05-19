from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


def home(request):
    context = {
        "posts": Post.objects.all().order_by("-date"),
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})


def contact(request):
    return render(request, "blog/contact.html", {"title": "Contacts"})


class PostListView(ListView):
    context_object_name = "posts"
    model = Post
    template_name = "blog/home.html"
    ordering = ["-date"]


class PostDetailView(DetailView):
    model = Post
