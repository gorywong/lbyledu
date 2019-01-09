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
    