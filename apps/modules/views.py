from django.shortcuts import render
from django.views.generic.base import View

from .models import SuperModules, SubModules
from article.models import Article

# Create your views here.

class EduInfoView(View):
    def get(self, request, sub_module_id):
        eduinfo = SuperModules.objects.get(name="教育信息")
        modules = SubModules.objects.filter(supermodules=eduinfo.id)
        current_module = SubModules.objects.get(id=int(sub_module_id))
        articles = Article.objects.filter(sort=current_module.id).order_by('-pub_date')
        articles = articles.filter(has_check=True).order_by('-pub_date')
        name = eduinfo.name
        return render(request, "eduinfo.html", {"name": name, "modules": modules, "sub_module_id": sub_module_id, "current_module": current_module, "articles": articles})


class ResearchView(View):
    def get(self, request, sub_module_id):
        research = SuperModules.objects.get(name="学科研究")
        modules = SubModules.objects.filter(supermodules=research.id)
        current_module = SubModules.objects.get(id=int(sub_module_id))
        articles = Article.objects.filter(sort=current_module.id).order_by('-pub_date')
        articles = articles.filter(has_check=True).order_by('-pub_date')
        name = research.name
        return render(request, "research.html", {"name": name, "modules": modules, "sub_module_id": sub_module_id, "current_module": current_module, "articles": articles})

                                            
class ResourceView(View):
    def get(self, request, sub_module_id):
        resource = SuperModules.objects.get(name="资源中心")
        modules = SubModules.objects.filter(supermodules=resource.id)
        current_module = SubModules.objects.get(id=int(sub_module_id))
        articles = Article.objects.filter(sort=current_module.id)
        articles = articles.filter(has_check=True).order_by('-pub_date')
        name = resource.name
        return render(request, "resource.html", {"name": name, "modules": modules, "sub_module_id": sub_module_id, "current_module": current_module, "articles": articles})


class PolicyView(View):
    def get(self, request, sub_module_id):
        policy = SuperModules.objects.get(name="政策法规")
        modules = SubModules.objects.filter(supermodules=policy.id)
        current_module = SubModules.objects.get(id=int(sub_module_id))
        articles = Article.objects.filter(sort=current_module.id).order_by('-pub_date')
        articles = articles.filter(has_check=True).order_by('-pub_date')
        name = policy.name
        return render(request, "policy.html", {"name": name, "modules": modules, "sub_module_id": sub_module_id, "current_module": current_module, "articles": articles})


class ShowView(View):
    def get(self, request, sub_module_id):
        show = SuperModules.objects.get(name="学校风采")
        modules = SubModules.objects.filter(supermodules=show.id)
        current_module = SubModules.objects.get(id=int(sub_module_id))
        articles = Article.objects.filter(sort=current_module.id).order_by('-pub_date')
        articles = articles.filter(has_check=True).order_by('-pub_date')
        name = show.name
        return render(request, "show.html", {"name": name, "modules": modules, "sub_module_id": sub_module_id, "current_module": current_module, "articles": articles})