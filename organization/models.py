#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-08 15:27:21
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-08 15:27:21
@Description:
"""
import logging
from abc import abstractmethod

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.functional import cached_property
from django.utils.timezone import now
from django.urls import reverse
from lbyledu.utils import cache_decorator, cache

logger = logging.getLogger(__name__)


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField(default=now, verbose_name="创建时间")
    last_mod_time = models.DateTimeField(default=now, verbose_name="修改时间")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

    @abstractmethod
    def get_absolute_url(self):
        pass


class Organization(BaseModel):
    CATEGORY_CHOICES = (
        ('center', '中心学校'),
        ('middle', '中学'),
        ('primary', '小学'),
        ('kindergarten', '幼儿园')
    )
    name = models.CharField(max_length=50, verbose_name="单位名称")
    category = models.CharField(choices=CATEGORY_CHOICES, default='center', max_length=12, verbose_name="分类")
    views = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    address = models.CharField(max_length=150, verbose_name="地址")
    website = models.CharField(max_length=100, null=True, blank=True, verbose_name="网址")
    telephone = models.CharField(max_length=20, verbose_name="联系电话")
    desc = RichTextUploadingField(verbose_name="概况")

    class Meta:
        verbose_name = "单位信息"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('organization:org_detail', kwargs={
            'org_category': self.category,
            'org_id': self.id
        })

    def viewed(self):
        self.veiws += 1
        self.save(update_fields=['views'])


class Leader(BaseModel):
    GENDER_CHOICES = (
        ("male", "男"),
        ("female", "女")
    )
    name = models.CharField(max_length=20, verbose_name="姓名")
    gender = models.CharField(choices=GENDER_CHOICES, default="male", max_length=6, verbose_name="性别")
    views = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="单位")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="联系电话")
    desc = RichTextUploadingField(verbose_name="简介")

    class Meta:
        verbose_name = "领导介绍"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def viewed(self):
        self.veiws += 1
        self.save(update_fields=['views'])