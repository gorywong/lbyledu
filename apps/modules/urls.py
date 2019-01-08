# -*- coding: utf-8 -*-

from django.urls import path, include

from .views import EduInfoView, ResearchView, ResourceView, PolicyView, ShowView

app_name = 'modules'
urlpatterns = [
    path('eduinfo/<int:sub_module_id>', EduInfoView.as_view(), name="eduinfo"),
    path('research/<int:sub_module_id>', ResearchView.as_view(), name="research"),
    path('resource/<int:sub_module_id>', ResourceView.as_view(), name="resource"),
    path('policy/<int:sub_module_id>', PolicyView.as_view(), name="policy"),
    path('show/<int:sub_module_id>', ShowView.as_view(), name="show"),
]