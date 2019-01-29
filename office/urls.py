#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-23 14:43:39
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-23 14:43:39
@Description:
"""
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import OfficeView, DocumentDetailView, DocumentAllListView, DocumentNotSignedListView, DocumentPublishView
from .views import ArticleManageListView, ArticleManageAllListView, ArticlePublishView, ArticleDeleteView, ArticleUpdateView
from .views import UserManageView
from .views import AddressBookView

app_name = 'office'
urlpatterns = [
    path('', login_required()(OfficeView.as_view()), name="index"),
    path('document/', login_required()(DocumentNotSignedListView.as_view()), name="document"),
    path('document/all/', login_required()(DocumentAllListView.as_view()), name="document_all"),
    path('document/publish/', login_required()(DocumentPublishView.as_view()), name="document_publish"),
    path('document/<int:number>', login_required()(DocumentDetailView.as_view()), name="document_detail"),
    path('article/', login_required()(ArticleManageListView.as_view()), name="article"),
    path('article/all/', login_required()(ArticleManageAllListView.as_view()), name="article_all"),
    path('article/publish/', login_required()(ArticlePublishView.as_view()), name="article_publish"),
    path('article/update/<int:article_id>', login_required()(ArticleUpdateView.as_view()), name="article_update"),
    path('article/delete/<int:article_id>', login_required()(ArticleDeleteView.as_view()), name="article_delete"),
    path('user/', login_required()(UserManageView.as_view()), name="user"),
    path('addressbook/', login_required()(AddressBookView.as_view()), name="address_book"),
]