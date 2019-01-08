# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from modules.models import SubModules
from organization.models import OrgDict

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="标题")
    sort = models.ForeignKey(SubModules, on_delete=models.CASCADE, verbose_name="板块")
    pub_date = models.DateTimeField(default=datetime.now, verbose_name="发布时间")
    origin = models.ForeignKey(OrgDict, on_delete=models.CASCADE, verbose_name="来源", default=1)
    author = models.CharField(max_length=20, verbose_name="作者")
    click_nums = models.IntegerField(default=0, verbose_name="点击量")
    content = RichTextUploadingField(verbose_name="内容")
    has_check = models.BooleanField(default=False, verbose_name="是否审核")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
