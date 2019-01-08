#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-08 17:11:39
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-08 17:11:39
@Description:
"""
from django.contrib import admin
from .models import Organization, Leader

# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'address')
    list_display_links = ('name',)
    search_fields = ('name', 'desc')
    list_filter = ('category',)

class LeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'organization', 'mobile')
    search_fields = ('name', 'organization')
    list_filter = ('gender', 'organization')

