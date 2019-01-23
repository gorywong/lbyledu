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
from .views import OfficeView, DocumentDetailView, DocumentListView, UserManageView
from django.contrib.auth.decorators import login_required

app_name = 'office'
urlpatterns = [
    path('', login_required()(OfficeView.as_view()), name='index'),
    path('document/', login_required()(DocumentListView.as_view()), name='document'),
    path('document/<int:number>', login_required()(DocumentDetailView.as_view()), name='document_detail'),
    path('usermanagement/', login_required()(UserManageView.as_view()), name='user_manage')
]