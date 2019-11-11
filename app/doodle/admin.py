from django.contrib import admin
from doodle.models import Post, Comment, Tag


@admin.register(Post)
class AdminPost(admin.ModelAdmin):

    list_display = ('author', 'text',)


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):

    list_display = ('author', 'text',)

@admin.register(Tag)
class AdmonTag(admin.ModelAdmin):

    list_display = ('title',)