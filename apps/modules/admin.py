from django.contrib import admin
from .models import SuperModules, SubModules

# Register your models here.

class SuperModulesAdmin(admin.ModelAdmin):
    list_display = ('name', 'add_time')
    search_fields = ('name',)
    list_filter = ('name', 'add_time')

class SubModulesAdmin(admin.ModelAdmin):
    list_display = ('name', 'supermodules', 'add_time')
    search_fields = ('name', 'supermodules')
    list_filter = ('supermodules', 'add_time')


admin.site.register(SuperModules, SuperModulesAdmin)
admin.site.register(SubModules, SubModulesAdmin)