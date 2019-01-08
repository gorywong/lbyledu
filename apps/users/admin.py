from django.contrib import admin
from .models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'realname', 'organization', 'position', 'mobile')
    search_fields = ('username', 'realname', 'organization', 'position', 'mobile')
    list_filter = ('username', 'realname', 'organization', 'position', 'mobile')


admin.site.register(UserProfile, UserProfileAdmin)