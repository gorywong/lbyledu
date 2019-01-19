#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-08 14:55:32
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-08 14:55:32
@Description:
"""
from django.urls import path, include
from .views import ArticleListView, ArticleDetailView, DevelopView

app_name = 'article'
urlpatterns = [
    path('developing/', DevelopView.as_view(), name="developing"),
    path('category/<int:parent_id>/<int:child_id>', ArticleListView.as_view(), name="category_detail"),
    path('article/<int:year>/<int:month>/<int:day>/<int:article_id>', ArticleDetailView.as_view(), name="detail_by_id")
]