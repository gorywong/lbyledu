#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-08 16:03:08
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-08 16:03:08
@Description:
"""
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden

from .models import Article, Category, Index, Banner


class IndexView(ListView):
    model = Index
    template_name = 'index.html'
    extra_context = {'banner_list': Banner.objects.all()}
    context_object_name = 'category_list'


class ArticleListView(ListView):
    model = Article
    template_name = 'article_index.html'
    context_object_name = 'article_list'
    paginate_by = settings.PAGINATE_BY

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('child_id'))
        return super(ArticleListView, self).get_queryset().filter(category=cate)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object()
        obj.viewed()
        self.object = obj
        return obj

    def get_context_data(self, **kwargs):
        articleid = int(self.kwargs[self.pk_url_kwarg])
        kwargs['next_article'] = self.object.next_article
        kwargs['prev_article'] = self.object.prev_article
        return super(ArticleDetailView, self).get_context_data(**kwargs)