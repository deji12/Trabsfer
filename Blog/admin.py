from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'number_of_comments', 'date']

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'email', 'website']

admin.site.register(Comment, CommentAdmin)