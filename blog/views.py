from django.shortcuts import render
# from django.views import generic, View
from django.views.generic import ListView, DetailView
from .models import BlogPost


# Posts Page View
class BlogPostList(ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-created_date')
    template_name = "posts.html"
    paginate_by = 6

    def index(request):
        """View to see posts page"""
        return render(request, "posts.html")



#def home(request):
    #return render(request, 'index.html', {})
