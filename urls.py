from django.urls import path, include
from django.contrib import admin
from users import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", views.register, name="register"),
    path("", include("blog.urls")),
    path("blogs/", include("blogs.urls")),
]
