from django.contrib import admin
from .models import Post, Comment


class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}  # automatic add slug field when add title
    raw_id_fields = ('author',)  # add user by id
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Post, AdminPost)


class AdminComment(admin.ModelAdmin):
    list_display = ['post', 'name', 'email', 'publish', 'active']
    search_fields = ['email', 'post', 'email']
    list_filter = ['active', 'publish', 'post']


admin.site.register(Comment, AdminComment)
