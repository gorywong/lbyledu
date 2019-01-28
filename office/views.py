#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-23 14:44:27
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-23 14:44:27
@Description:
"""
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import REDIRECT_FIELD_NAME
from article.models import Article, Category
from users.models import UserProfile, UserGroup
from article.models import Article
from .models import Document
from .forms import DocumentPublishForm, ArticlePublishForm

# Create your views here.
class BaseOfficeListView(ListView):
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


class OfficeView(ListView):
    model = Document
    template_name = 'office/office_index.html'
    context_object_name = 'documents'
    extra_context = {'notices': Article.objects.filter(category__name='最新公告', has_check=True, status='p').order_by('-pub_date')[:8],
                     'notice_cate': Category.objects.get(name='最新公告')}

    def get_queryset(self, *args, **kwargs):
        super(OfficeView, self).get_queryset(*args, **kwargs)
        documents = Document.objects.all().filter(receiver__id=self.request.user.id)[:10]
        
        return documents
    
    def get_context_data(self, *args, **kwargs):
        context = super(OfficeView, self).get_context_data(**kwargs)
        documents = Document.objects.all().filter(receiver__id=self.request.user.id)
        not_signed_documents = documents.exclude(checked_receiver__id=self.request.user.id)[:10]
        context['not_signed_document_list'] = not_signed_documents

        return context


class DocumentDetailView(DetailView):
    pass


class DocumentNotSignedListView(BaseOfficeListView):
    model = Document
    template_name = 'office/document_list.html'
    context_object_name = 'document_list'
    paginate_by = settings.PAGINATE_BY

    def get_queryset(self, *args, **kwargs):
        super(DocumentNotSignedListView, self).get_queryset(*args, **kwargs)
        documents = Document.objects.all().filter(receiver__id=self.request.user.id).exclude(checked_receiver__id=self.request.user.id)
        
        return documents
    
    def get_context_data(self, **kwargs):
        context = super(DocumentNotSignedListView, self).get_context_data(**kwargs)

        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        return context


class DocumentAllListView(BaseOfficeListView):
    model = Document
    template_name = 'office/document_list.html'
    context_object_name = 'document_list'
    paginate_by = settings.PAGINATE_BY

    def get_queryset(self, *args, **kwargs):
        super(DocumentAllListView, self).get_queryset(*args, **kwargs)
        documents = Document.objects.all().filter(receiver__id=self.request.user.id)
        
        return documents
    
    def get_context_data(self, **kwargs):
        context = super(DocumentAllListView, self).get_context_data(**kwargs)

        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        return context


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

    def form_valid(self, form):
        if form.is_valid():
            receiver_group_id = form.cleaned_data['receiver_group']
            num = str(form.cleaned_data['number'])
            if len(num) == 1:
                num = '0' + num
            number = datetime.now().strftime("%Y%m%d") + num
            if Document.objects.filter(number=number):
                form._errors['number_exists'] = '* 该编号已存在'
                return self.render_to_response({'form': form})

            document = Document.objects.create(
                title=form.cleaned_data['title'],
                author=self.request.user,
                content=form.cleaned_data['content'],
                receiver_group=UserGroup.objects.get(id=receiver_group_id),
                number=number,
            )
            users = UserProfile.objects.filter(usergroups__id=receiver_group_id)
            document.receiver.add(*users)

            return super(DocumentPublishView, self).form_valid(form)
        else:
            return self.render_to_response({'form': form})


class ArticleManageListView(BaseOfficeListView):
    model = Article
    template_name = 'office/article_list.html'
    context_object_name = 'article_list'
    paginate_by = settings.PAGINATE_BY

    def get_queryset(self, *args, **kwargs):
        super(ArticleManageListView, self).get_queryset(*args, **kwargs)
        article_list = Article.objects.filter(has_check=False)
        
        return article_list
    
    def get_context_data(self, **kwargs):
        context = super(ArticleManageListView, self).get_context_data(**kwargs)

        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        return context


class ArticleManageAllListView(BaseOfficeListView):
    model = Article
    template_name = 'office/article_list.html'
    context_object_name = 'article_list'
    paginate_by = settings.PAGINATE_BY

    def get_queryset(self, *args, **kwargs):
        super(ArticleManageAllListView, self).get_queryset(*args, **kwargs)
        article_list = Article.objects.all()
        
        return article_list
    
    def get_context_data(self, **kwargs):
        context = super(ArticleManageAllListView, self).get_context_data(**kwargs)

        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        return context


class ArticlePublishView(FormView):
    template_name = 'office/article_publish.html'
    form_class = ArticlePublishForm
    success_url = '/'
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        return super(ArticlePublishView, self).dispatch(request, *args, **kwargs)
    


class UserManageView(BaseOfficeListView):
    model = UserProfile
    template_name = 'office/user_manage.html'
    context_object_name = 'user_list'
    paginate_by = settings.PAGINATE_BY

    def get_queryset(self, *args, **kwargs):
        super(UserManageView, self).get_queryset(*args, **kwargs)
        user_list = UserProfile.objects.filter(is_active=False)
        
        return user_list

    def get_context_data(self, **kwargs):
        context = super(UserManageView, self).get_context_data(**kwargs)

        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        return context

class AddressBookView(View):
    pass