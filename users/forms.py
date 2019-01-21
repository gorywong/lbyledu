#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-21 14:13:53
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-21 14:13:53
@Description:
"""
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import widgets
from django.conf import settings
from captcha.fields import CaptchaField, CaptchaTextInput

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = widgets.TextInput(attrs={'placeholder': '请输入用户名'})
        self.fields['password'].widget = widgets.PasswordInput(attrs={'placeholder': '请输入密码'})

class RegisterForm(UserCreationForm):
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = widgets.TextInput(attrs={'placeholder': '请输入用户名'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'placeholder': '请输入邮箱地址'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'placeholder': '请输入密码'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'placeholder': '请确认密码'})
        self.fields['captcha'].widget = CaptchaTextInput(attrs={'placeholder': '请输入验证码'})
        
    class Meta:
        model = get_user_model()
        fields = ("username", "email")