# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

from organization.models import OrgDict
# Create your models here.

class UserProfile(AbstractUser):
    realname = models.CharField(max_length=50, verbose_name="真实姓名", default="")
    level = models.CharField(max_length=50, verbose_name="级别", default="")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(choices=(("male", "男"), ("female", "女")), default="female", max_length=6, verbose_name="性别")
    organization = models.ForeignKey(OrgDict, on_delete=models.CASCADE, default="1", verbose_name="单位")
    position = models.CharField(choices=(("zxxxz", "中心校校长"), ("zxxz", "中学校长"), ("xxxz", "小学校长"), ("teacher", "教师")), default="teacher", max_length=7, verbose_name="职务")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="电话")


    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(choices=(("register", "注册"), ("forget", "找回密码")), max_length=10, verbose_name="验证码类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)