from django.contrib import admin
from user.models import Profile, Follow


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):

    list_display = ('user', 'birth_date',)


@admin.register(Follow)
class AdminFollow(admin.ModelAdmin):

    list_display = ('following', 'follow_time',)
