from django.contrib import admin
from .models import BlogPost, Category, Comments
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    prepopulated_fields = {('slug'): ('title',)}
    list_filter = ('status', 'created_date')
    list_display = ('title', 'slug', 'status', 'created_date')
    search_fields = ['title', 'content']


@admin.register(Comments)
class PostComment(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_date', 'approved')
    list_filter = ('approved', 'created_date')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Category)
