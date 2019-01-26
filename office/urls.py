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
from .views import ArticleManageListView, ArticleManageAllListView
from .views import AddressBookView

app_name = 'office'
urlpatterns = [
    path('', login_required()(OfficeView.as_view()), name="index"),
    path('document/', login_required()(DocumentNotSignedListView.as_view()), name="document"),
    path('document/all/', login_required()(DocumentAllListView.as_view()), name="document_all"),
    path('document/publish/', login_required()(DocumentPublishView.as_view()), name="document_publish"),
    path('document/<int:number>', login_required()(DocumentDetailView.as_view()), name="document_detail"),
    path('articlemanage/', login_required()(ArticleManageListView.as_view()), name="article_manage"),
    path('articlemanage/all/', login_required()(ArticleManageAllListView.as_view()), name="article_manage_all"),
    path('addressbook/', login_required()(AddressBookView.as_view()), name="address_book"),
]