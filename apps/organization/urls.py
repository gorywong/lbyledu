# -*- coding: utf-8 -*-

from django.urls import path, include

from .views import InfoView, LeaderInfoView

app_name = 'organization'
urlpatterns = [
    path('info/<int:org_id>', InfoView.as_view(), name="org_info"),
    path('leaderinfo/<int:leader_id>', LeaderInfoView.as_view(), name="leader_info")
]
