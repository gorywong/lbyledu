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
from django.conf import settings
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import REDIRECT_FIELD_NAME
from article.models import Article, Category
from users.models import UserProfile
from .models import Document
from .forms import DocumentPublishForm

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


class DocumentNotSignedListView(ListView):
    model = Document
    template_name = 'office/document_notsigned.html'
    context_object_name = 'document_list'
    paginate_by = settings.PAGINATE_BY

    def get_queryset(self, *args, **kwargs):
        super(DocumentNotSignedListView, self).get_queryset(*args, **kwargs)
        documents = Document.objects.all().order_by('-created_time')
        for document in documents:
            if self.request.user in document.checked_receiver.all():
                documents.pop(document)
        
        return documents
    
    def get_context_data(self, **kwargs):
        context = super(DocumentNotSignedListView, self).get_context_data(**kwargs)

        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}

        left = []
        right = []
        left_has_more = False
        right_has_more = False
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range

        if page_number == 1:
            right = page_range[page_number:page_number + 3]
            if right[-1] < total_pages - 1:
                right_has_more = True
        elif page_number == total_pages:
            left = page_range[(page_number - 2) if (page_number - 2) > 0 else 0:page_number - 1]
            if left[0] > 2:
                left_has_more = True
        else:
            left = page_range[(page_number - 2) if (page_number - 2) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 3]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if left[0] > 2:
                left_has_more = True

        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
        }

        return data


class DocumentAllListView(ListView):
    model = Document
    template_name = 'office/document_all.html'
    context_object_name = 'document_list'
    paginate_by = settings.PAGINATE_BY
    
    def get_context_data(self, **kwargs):
        context = super(DocumentAllListView, self).get_context_data(**kwargs)

        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}

        left = []
        right = []
        left_has_more = False
        right_has_more = False
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range

        if page_number == 1:
            right = page_range[page_number:page_number + 3]
            if right[-1] < total_pages - 1:
                right_has_more = True
        elif page_number == total_pages:
            left = page_range[(page_number - 2) if (page_number - 2) > 0 else 0:page_number - 1]
            if left[0] > 2:
                left_has_more = True
        else:
            left = page_range[(page_number - 2) if (page_number - 2) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 3]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if left[0] > 2:
                left_has_more = True

        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
        }

        return data


class DocumentPublishView(FormView):
    template_name = 'office/document_publish.html'
    form_class = DocumentPublishForm
    success_url = '/'
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        return super(DocumentPublishView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        user = self.request.user
        form_kwargs = super(DocumentPublishView, self).get_form_kwargs()
        form_kwargs.update({'user': UserProfile.objects.get(username=user.username)})
        return form_kwargs
        

class AddressBookView(View):
    pass