from django.contrib import admin
from .models import OrgDict, LeaderInfo

# Register your models here.

class OrgDictAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'sort', 'add_time')
    search_fields = ('name', 'address', 'sort')
    list_filter = ('sort', 'add_time')

class LeaderInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'organization', 'mobile', 'add_time')
    search_fields = ('name', 'gender', 'organization', 'mobile')
    list_filter = ('name', 'gender', 'organization', 'mobile', 'add_time')


admin.site.register(OrgDict, OrgDictAdmin)
admin.site.register(LeaderInfo, LeaderInfoAdmin)