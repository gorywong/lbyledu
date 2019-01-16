#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-08 17:51:35
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-08 17:51:35
@Description:
"""
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from lbyledu.logentryadmin import LogEntryAdmin
from article.admin import *
from organization.admin import *
from users.admin import *

class MyAdminSite(admin.AdminSite):
    site_header = '豫灵镇中心学校网站后台管理系统'
    site_title = '豫灵镇中心学校网站后台管理系统'

    def __init__(self, name='admin'):
        super().__init__(name)

    def has_permission(self, request):
        return request.user.is_superuser


admin_site = MyAdminSite(name='admin')

admin_site.register(Index, IndexAdmin)
admin_site.register(Article, ArticleAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Banner, BannerAdmin)
admin_site.register(SiteSetting, SiteSettingAdmin)

admin_site.register(Organization, OrganizationAdmin)
admin_site.register(Leader, LeaderAdmin)

admin_site.register(UserProfile, UserProfileAdmin)

admin_site.register(LogEntry, LogEntryAdmin)
