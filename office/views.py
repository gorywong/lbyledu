#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-23 14:44:27
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-23 14:44:27
@Description:
"""
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from article.models import Article, Category
from .models import Document

# Create your views here.
class OfficeView(ListView):
    model = Document
    template_name = 'office/office_index.html'
    queryset = Document.objects.all().order_by('-created_time')[:10]
    extra_context = {'notices': Article.objects.filter(category__name='最新公告', has_check=True, status='p').order_by('-pub_date')[:8],
                     'notice_cate': Category.objects.get(name='最新公告')}
    context_object_name = 'documents'


class DocumentDetailView(DetailView):
    pass


class DocumentListView(ListView):
    pass


class UserManageView(ListView):
    pass


class UserMessageView(View):
    pass

class AddressBookView(View):
    pass