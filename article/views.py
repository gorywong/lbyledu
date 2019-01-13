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

from .models import Article, Category


class ArticleListView(ListView):
    # template_name属性用于指定使用哪个模板进行渲染
    template_name = 'article_index.html'

    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）
    context_object_name = 'article_list'

    # 页面类型，分类目录或标签列表等
    paginate_by = settings.PAGINATE_BY
    page_kwarg = 'page'