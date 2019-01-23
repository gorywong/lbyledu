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
from .views import OfficeView
from django.contrib.auth.decorators import login_required

app_name = 'office'
urlpatterns = [
    path('office/', login_required()(OfficeView.as_view()), name='index'),
]