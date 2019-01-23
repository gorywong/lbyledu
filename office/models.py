#!/usr/bin/env python


"""
@Author: gorywong
@Date: 2019-01-23 15:15:01
@Software: Visual Studio Code
@Last Modified by: gorywong
@Last Modified time: 2019-01-23 15:15:01
@Description:
"""
import logging
from abc import abstractmethod

from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.functional import cached_property
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField

from lbyledu.utils import cache_decorator, cache
from users.models import UserGroup

logger = logging.getLogger(__name__)

# Create your models here.
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


class Document(BaseModel):
    title = models.CharField(max_length=200, unique=True, verbose_name="标题")
    receiver = models.ForeignKey(UserGroup, on_delete=models.CASCADE, verbose_name="收件用户组")
    # 编号
    # 是否已读