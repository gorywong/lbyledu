#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-24 14:05:49
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-24 14:05:49
@Description:
"""
from django.contrib import admin
from .models import Document, OrganizationAdmins

# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id', 'title', 'author','receiver_group', 'created_time')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('author', 'receiver_group')
    exclude = ('created_time', 'last_mod_time')
    view_on_site = True


class OrganizationAdminsAdmin(admin.ModelAdmin):
    list_display = ('organization', 'admin')
    list_display_links = ('organization', 'admin')
    list_filter = ('organization',)