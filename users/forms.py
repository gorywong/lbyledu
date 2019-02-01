#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-21 14:13:53
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-21 14:13:53
@Description:
"""
import re
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import widgets
from django.conf import settings
from captcha.fields import CaptchaField, CaptchaTextInput
from .models import EmailVerifyRecord

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = widgets.TextInput(attrs={'placeholder': '请输入用户名或邮箱地址'})
        self.fields['password'].widget = widgets.PasswordInput(attrs={'placeholder': '请输入密码'})


class RegisterForm(UserCreationForm):
    DEFAULT_ERROR_MESSAGES = {'required': '请填写该字段', 'invalid_choice': '请正确填写该字段'}
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"}, widget=CaptchaTextInput(attrs={'placeholder': '请输入验证码'}))

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = widgets.TextInput(attrs={'placeholder': '请输入用户名'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'placeholder': '请输入邮箱地址'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'placeholder': '请输入密码'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'placeholder': '请确认密码'})

        self.fields['username'].error_messages = self.DEFAULT_ERROR_MESSAGES
        self.fields['email'].error_messages = self.DEFAULT_ERROR_MESSAGES
        self.fields['password1'].error_messages = self.DEFAULT_ERROR_MESSAGES
        self.fields['password2'].error_messages = self.DEFAULT_ERROR_MESSAGES

    def is_valid(self):
        valid = super(RegisterForm, self).is_valid()

        if not valid:
            return valid

        if not re.match('^[A-Za-z0-9]+$', self.cleaned_data['username']):
            self._errors['invalid_username'] = '* 用户名只能包含数字或字母'
            return False

        return True
        
    class Meta:
        model = get_user_model()
        fields = ("username", "email")