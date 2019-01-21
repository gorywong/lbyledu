#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-22 01:51:51
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-22 01:51:51
@Description:
"""
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailOrUsernameModelBackend(ModelBackend):
    """
    允许使用用户名或邮箱登陆
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = get_user_model().objects.get(**kwargs)
            if user.check_password(password):
                return user
        except get_user_model().DoesNotExist:
            return None
        
    def get_user(self, username):
        try:
            return get_user_model().objects.get(pk=username)
        except get_user_model().DoesNotExist:
            return None