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
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
class OfficeView(TemplateView):
    template_name = 'office/office_index.html'


class DocumentDetailView(DetailView):
    pass


class DocumentListView(ListView):
    pass


class UserManageView(ListView):
    pass