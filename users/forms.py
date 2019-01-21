#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-21 14:13:53
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-21 14:13:53
@Description:
"""
from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)

class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
    password_determine = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})