# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class OrgDict(models.Model):
    name = models.CharField(max_length=50, verbose_name="单位")
    sort = models.CharField(choices=(("center", "中心学校"), ("middle", "中学"), ("primary", "小学"), ("kindergarten", "幼儿园")), default="center", max_length=12, verbose_name="类别")
    address = models.CharField(max_length=150, verbose_name="地址")
    website = models.CharField(max_length=100, null=True, blank=True, verbose_name="网址")
    telephone = models.CharField(max_length=20, verbose_name="联系电话")
    desc = RichTextField(verbose_name="概况")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "单位信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class LeaderInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名")
    gender = models.CharField(choices=(("male", "男"), ("female", "女")), default="female", max_length=6, verbose_name="性别")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    organization = models.ForeignKey(OrgDict, on_delete=models.CASCADE, verbose_name="单位")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="电话")
    desc = RichTextField(verbose_name="简介")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "领导介绍"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name