from django.shortcuts import render
from django.views.generic.base import View

from modules.models import SuperModules, SubModules
from .models import Article
# Create your views here.

class ArticleView(View):
    def get(self, request, article_id):
        article = Article.objects.get(id=int(article_id))
        if article :
            if article.has_check == True:
                title = article.title
                origin = article.origin
                author = article.author
                click_nums = article.click_nums
                pub_date = article.pub_date.strftime('%Y-%m-%d %H:%M:%S')
                content = article.content
                sub_module_id = article.sort_id
                sub_module = SubModules.objects.get(id=int(sub_module_id))
                super_module_id = sub_module.supermodules_id
                sub_modules = SubModules.objects.filter(supermodules_id=super_module_id)
                super_module = SuperModules.objects.get(id=int(super_module_id))

                return render(request, 'article.html', {"title": title, "origin": origin, "author": author, "click_nums": click_nums, "pub_date": pub_date, "content": content, "sub_module": sub_module,"sub_modules": sub_modules, "super_module": super_module})
            else:
                return render(request, '404.html', status=404)
        else:
            return render(request, '404.html', status=404)


class IndexView(View):
    def get(self, request):
        all_articles = Article.objects.all()
        return render(request, "index.html", {"all_articles": all_articles})