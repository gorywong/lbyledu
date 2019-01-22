#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-21 16:00:03
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-21 16:00:03
@Description:
"""
from django.urls import path, include
from .views import LoginView, RegisterView, LogoutView
from .forms import LoginForm

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name="login", kwargs={'authentication_form': LoginForm}),
    path('register/', RegisterView.as_view(), name="register"),
    path('logout/', LogoutView.as_view(), name="logout")
]