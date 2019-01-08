#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-08 15:51:37
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-08 15:51:37
@Description:
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.timezone import now

from organization.models import Organization


class UserProfile(AbstractUser):
    POSITION_CHOICES = (
        ("zxxxz", "中心校校长"),
        ("zxxz", "中学校长"),
        ("xxxz", "小学校长"),
        ("teacher", "教师")
    )
    GENDER_CHOICES = (
        ("male", "男"),
        ("female", "女")
    )
    realname = models.CharField(max_length=50, verbose_name="真实姓名", default="")
    level = models.CharField(max_length=50, verbose_name="级别", default="")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, default="male", max_length=6, verbose_name="性别")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default="1", verbose_name="单位")
    position = models.CharField(choices=POSITION_CHOICES, default="teacher", max_length=7, verbose_name="职务")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="电话")
    create_time = models.DateTimeField(default=now, verbose_name="创建时间")
    last_mod_time = models.DateTimeField(default=now, verbose_name="修改时间")
    first_name = None
    last_name = None

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.realname


class EmailVerifyRecord(models.Model):
    SEND_TYPE_CHOICES = (
        ("register", "注册"),
        ("forget", "找回密码")
    )
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(choices=SEND_TYPE_CHOICES, max_length=8, verbose_name="验证码类型")
    send_time = models.DateTimeField(default=now, verbose_name="发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)