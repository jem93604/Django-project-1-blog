from django.urls import path, include
from django.contrib import admin
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", views.register, name="register"),
    path("", include("blog.urls")),
    path(
        "logout",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path(
        "login",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("blogs/", include("blogs.urls")),
]
