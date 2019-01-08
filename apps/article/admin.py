from django.contrib import admin
from .models import Article

# Register your models here.
def make_checked(modeladmin, request, queryset):
    queryset.update(has_check=True)
    make_checked.short_description = "审核所选的 文章"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'sort', 'origin', 'author', 'has_check', 'pub_date')
    search_fields = ('title', 'origin', 'author')
    list_filter = ('sort', 'origin', 'pub_date')
    actions = [make_checked]


admin.site.register(Article, ArticleAdmin)