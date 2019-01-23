from django.contrib import admin
from .models import UserProfile, UserGroup

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'realname', 'organization', 'position', 'mobile')
    list_display_links = ('username', 'realname')
    search_fields = ('realname', 'position')
    list_filter = ('organization', 'position')


class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')