#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-08 16:03:24
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-08 16:03:24
@Description:
"""
from django.urls import path, include

#from .views import InfoView, LeaderInfoView

app_name = 'organization'
urlpatterns = [
    #path('organization/<org_category>/<int:org_id>', InfoView.as_view(), name="org_detail"),
    #path('leaderdetail/<int:leader_id>', LeaderInfoView.as_view(), name="leader_detail")
]
