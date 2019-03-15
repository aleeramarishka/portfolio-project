from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblogs(request):
    allblogs = Blog.objects
    return render(request, 'blog/home.html', {'allblogs':allblogs})

def blogdetails(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blogdetails.html', {'details':details})

    