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
from django.contrib.auth.decorators import login_required
from .views import LoginView, RegisterView, LogoutView, PasswordChangeView, UserProfileView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import LoginForm

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name="login", kwargs={'authentication_form': LoginForm}),
    path('register/', RegisterView.as_view(), name="register"),
    path('logout/', login_required()(LogoutView.as_view()), name="logout"),
    path('passwordchange/', login_required()(PasswordChangeView.as_view()), name="password_change"),
    path('user/<username>/', login_required()(UserProfileView.as_view()), name="user_profile"),
    path('user/password/reset/', PasswordResetView.as_view(), name="password_reset"),
    path('user/password/reset/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('user/password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('user/reset/done/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]