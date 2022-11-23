from django.contrib import admin
from .models import BlogPost, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')


admin.site.register(Category)