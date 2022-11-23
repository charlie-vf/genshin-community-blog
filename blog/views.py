from django.shortcuts import render
from django.views import generic, View
from .models import BlogPost


class BlogPostList(generic.ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-created_date')
    template_name = 'index.html'
    paginate_by = 6
