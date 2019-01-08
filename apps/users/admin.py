from django.contrib import admin
from .models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'realname', 'organization', 'position', 'mobile')
    list_display_links = ('username', 'realname')
    search_fields = ('realname', 'position')
    list_filter = ('organization', 'position')

