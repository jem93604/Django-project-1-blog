from django.shortcuts import render


posts = [
    {
        "author": "Jos Ephraim",
        "title": "Blog Post 1",
        "comment": "First post content",
        "date": "August 27, 2023",
    },
    {
        "author": "zuckerberg",
        "title": "just found the goat",
        "comment": "this is the greatest social media platform",
        "date": "August 27, 2023",
    },
]


def home(request):
    context = {
        "posts": posts,
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html",{'title':'About'})


def contact(request):
    return render(request, "blog/contact.html",{'title':'Contacts'})
