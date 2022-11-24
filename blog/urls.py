from django.urls import path
from .views import BlogPostList

urlpatterns = [
    # path('', views.home, name='home'),
    path('', BlogPostList.as_view(), name='all_posts'),
]
