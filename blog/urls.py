from django.urls import path
from . import views
from .views import (
    PostCreateView,
    PostDeleteView,
    PostListView,
    PostDetailView,
    PostUpdateView,
    UserPostListview,
)

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("user/<str:username>/", UserPostListview.as_view(), name="user-posts"),
    path("about/", views.about, name="blog-about"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"),
    path("post/new", PostCreateView.as_view(), name="post-create"),
    path("user/<str:username>/", UserPostListview.as_view(), name="user-posts"),
]
