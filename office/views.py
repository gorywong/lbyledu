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
    context_object_name = 'documents'
    extra_context = {'notices': Article.objects.filter(category__name='最新公告', has_check=True, status='p').order_by('-pub_date')[:8],
                     'notice_cate': Category.objects.get(name='最新公告')}

    def get_context_data(self, *args, **kwargs):
        context = super(OfficeView, self).get_context_data(**kwargs)
        documents = Document.objects.all().order_by('-created_time')
        not_signed_documents = []
        count = 0
        for document in documents:
            if self.request.user not in document.checked_receiver.all():
                not_signed_documents.append(document)
                count += 1
            if count == 10:
                break

        context['not_signed_document_list'] = not_signed_documents
        return context


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