from django.contrib import admin
from .models import Article, Category, Banner, SiteSetting

# Register your models here.
def make_checked(modeladmin, request, queryset):
    queryset.update(has_check=True)

def draft_article(modeladmin, request, queryset):
    queryset.update(status='d')

make_checked.short_description = "审核所选的 文章"
draft_article.short_description = '将选中的文章设置为草稿'

class ArticleAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id', 'title', 'category', 'origin', 'author', 'views','has_check', 'status','pub_date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('category', 'origin', 'status', 'has_check')
    exclude = ('created_time', 'last_mod_time')
    view_on_site = True
    actions = [make_checked, draft_article]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BannerAdmin(admin.ModelAdmin):
    list_display = ('id','article')
    list_display_links = ('id', 'article')

class SiteSettingAdmin(admin.ModelAdmin):
    pass
