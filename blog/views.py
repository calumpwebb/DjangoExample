from django.shortcuts import render

# Create your views here.
posts = [
    {
        "author": "Calum",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "August 27th 2020",
    },
    {
        "author": "John",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "August 28th 2020",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    context = {"title": "About"}
    return render(request, "blog/about.html", context)
