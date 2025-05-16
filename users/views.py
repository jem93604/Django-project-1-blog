from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import userRegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"account created for {username} You can now log in "
            )
            return redirect("login")
    else:
        form = userRegisterForm()
    return render(request, "users/register.html", {"form": form})


def profile(request):
    return render(request, "users/profile.html")
