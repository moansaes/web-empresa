from django.shortcuts import render
from blog.models import Post

def blog(request):
    post=Post.objects.all()
    return render(request, "blog/blog.html", {"post":post})